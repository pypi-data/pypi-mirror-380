from typing import List
from src.chunking import count_tokens
from src.chroma_storage import query_chroma, count_documents_in_collection, DocumentMatch
from src.config_model import Config
from src.rerank import Reranker
from src.services.llm_service import LLMService
from src.logging import save_chat_history


def safe_gpt_call(query: str, chunks: List[DocumentMatch], model: str, tpm_limit, llm_service: LLMService) -> str:
    system_prompt = "Du er en dansk juristassistent. Besvar spørgsmålet konkret og faktuelt baseret kun på konteksten nedenfor."
    max_tokens = tpm_limit
    #while count_tokens(system_prompt + "\n\n" + "\n\n".join(chunks), model) > max_tokens and chunks:
    #    chunks.pop()
    #    print("removing chunk, this should be reviced")
    return generate_answer(query, chunks, model, llm_service=llm_service)

def generate_answer(query: str, context_chunks: List[DocumentMatch], model: str, llm_service: LLMService) -> str:

    context = "\n\n".join(
        f"[Kilde: {chunk.doc_id}]\n{chunk.document}" for chunk in context_chunks
    )

    user_prompt = f"Kontekst:\n{context}\n\nSpørgsmål:\n{query}"
    response = llm_service.get_response(
        model=model,
        messages=[
            {
                "role": "system",
                "content": (
                    "Du er en juridisk assistent drevet af et RAG-system. "
                    "Din opgave er at hjælpe jurapersonale med at finde præcise og relevante oplysninger i dokumenter. "
                    "Besvar kun spørgsmål, hvis svaret fremgår direkte og utvetydigt af konteksten. "
                    "Hvis noget bliver spurgt, f.eks. 'Hvornår siger personen det til lægen første gang?', må du kun svare, "
                    "hvis det eksplicit fremgår, at personen siger det direkte til lægen. "
                    "Antagelser, fortolkninger eller indirekte formuleringer må ikke bruges som grundlag for et svar. "
                    "Hvis informationen ikke fremgår tydeligt, skal du svare: 'Det fremgår ikke af materialet.'"
                    "Returner det dokument navn, hvor du med størst sandsynlighed har fundet information til det givne svar"
                )
            },
            {"role": "user", "content": user_prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def rewrite_query(raw_query: str, doc_type: str, llm_service: LLMService, model: str) -> str:
    prompt = (
        f"Du er en juridisk assistent. Omskriv følgende spørgsmål, så det bliver entydigt og velegnet til søgning i dokumenter "
        f"om {doc_type}. Medtag alle nødvendige detaljer, så det ikke kræver forudgående kontekst.\n\n"
        f"Spørgsmål: {raw_query}"
    )
    response = llm_service.get_response(
        model=model,
        messages=[{"role": "system", "content": "Du hjælper med at forbedre søgninger i juridiske dokumenter."},
                  {"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()


def get_chunks(config: Config, db_dir: str, collection_name: str, llm_service: LLMService, reranker: Reranker, query: str) -> List[DocumentMatch]:

    if config.query.improve_query:
        query = rewrite_query(
            query, 
            doc_type="arbejdsskadesager", 
            llm_service=llm_service, 
            model=config.query.model
        )
        print(f"Rewritten query: {query}")

    query_embedding = llm_service.get_embeddings(
        query, 
        config.embedding.model
    )

    initial_chunks: List[DocumentMatch] = query_chroma(
        query_embedding,
        db_dir,
        collection_name,
        method=config.chroma.method,
        threshold=config.chroma.threshold
    )

    print(f"Initial chunks -> Number of documents found: {len(initial_chunks)} out of {count_documents_in_collection(db_dir, collection_name)}")

    top_chunks = reranker.rerank_documents(query, initial_chunks)

    print(f"After reranking -> Number of documents found: {len(top_chunks)} out of {count_documents_in_collection(db_dir, collection_name)}")

    return top_chunks


def interactive_query_loop(config: Config, db_dir: str, collection_name: str, llm_service: LLMService, reranker: Reranker) -> None:

    print("\n💬 Skriv dit spørgsmål (eller 'exit' for at afslutte):\n")
    
    user_id = input("👤 Indtast bruger-ID (eller tryk Enter for 'anonymous'): ").strip() or "anonymous"
    if user_id.lower() in {"exit", "quit", "afslut"}:
        print("👋 Afslutter.")
        return

    while True:
        query = input("🔎 Spørgsmål: ").strip()
        if query.lower() in {"afslut", "exit", "quit"}:
            print("👋 Afslutter.")
            break

        top_chunks = get_chunks(
            config,
            db_dir,
            collection_name,
            llm_service,
            reranker,
            query
        )

        for chunk in top_chunks:
            print(chunk.doc_id)

        answer = safe_gpt_call(
            query,
            top_chunks,
            config.query.model,
            config.query.max_tokens,
            llm_service
        )
        print("\n✅ Svar genereret:\n")
        print(answer)
        
        # Save chat history
        save_chat_history(user_id, query, answer)