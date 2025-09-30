from pathlib import Path
from typing import Optional
import re
from datetime import datetime
from PyPDF2 import PdfReader, PdfWriter, PdfMerger
from pydantic import BaseModel, Field
from pathlib import Path
from dotenv import load_dotenv
from src.services.llm_service import LLMService

load_dotenv(dotenv_path=Path(__file__).resolve().parents[1] / ".env")


class JournalNotat(BaseModel):
    """
    Represents a single journal note with text, date and unique id.
    """
    text: str = Field(..., description="The text content of the journal note.")
    date: str = Field(..., description="The date of the journal note in YYYY-MM-DD format.")
    id: int = Field(..., description="An incremental identifier for the journal note.")

class JournalNotater(BaseModel):
    """
    Represents a collection of journal notes.
    """
    
    notes: list[JournalNotat] = Field(
        default_factory=list,
        description="A list of journal notes, each with its own text, date, and id."
    )   


def split_pdf_by_bookmarks(
        input_pdf_path: Path,
        output_dir: Path,
        title_prefix: Optional[str] = None,
) -> None:
    reader = PdfReader(str(input_pdf_path))
    outlines = reader.outline

    if not output_dir.exists():
        output_dir.mkdir(parents=True)

    bookmark_pages = []

    for entry in outlines:
        if isinstance(entry, list):
            continue  # skip nested bookmarks

        title = entry.title.strip().replace("/", "-").replace("\\", "-")
        page_index = reader.get_destination_page_number(entry)
        bookmark_pages.append((title, page_index))

    # Sort and pair start-end ranges
    bookmark_pages.sort(key=lambda x: x[1])
    for i, (title, start_page) in enumerate(bookmark_pages):
        end_page = bookmark_pages[i + 1][1] if i + 1 < len(bookmark_pages) else len(reader.pages)

        writer = PdfWriter()
        for page_num in range(start_page, end_page):
            writer.add_page(reader.pages[page_num])

        filename = f"{title_prefix or ''}{title}.pdf"
        output_path = output_dir / filename
        with open(output_path, "wb") as f:
            writer.write(f)



def get_journalnotat(llm_service: LLMService, 
                     first_text: str, 
                     first_text_id: str, 
                     first_text_date: str, 
                     second_text: str, 
                     model: str, 
                     output_path: Path) -> str:

    """
    Concatenates two journal notes if they belong to the same journal entry.
    If the first text is empty, it creates a new journal note with a new id and date.
    Args:
        llm_service (LLMService): The LLM service to use for processing.
        first_text (str): The text of the first journal note.
        first_text_id (str): The id of the first journal note.
        first_text_date (str): The date of the first journal note.
        second_text (str): The text of the second journal note.
        model (str): The model to use for processing.
        output_path (Path): The directory where the journal notes will be saved.
    Returns:
        tuple: A tuple containing the concatenated journal note text, its id, and date.
    """
    user_prompt = f"""Id of first text: {first_text_id}
                      --
                      Date of first text: {first_text_date}
                      --
                      First text: '{first_text}'
                      --
                      Second text: '{second_text}'
                      --
                    """
    
    journalnotes = llm_service.get_response(
    model=model,
    messages=[
        {
            "role": "system",
            "content": (
                """You are an expert document analyst.
                   Your job is to split a document into journalnotes.
                   You are about to be shown two texts: the first text is (part of) the last journalnote
                   of the previous analysis. The second text is a new list of journalnotes, the first of which
                   may or may not be part of the last journalnote of the previous analysis. 
                   If there is no indication that the first part of the second text is a new journalnote, concatenate 
                   it to the first text creating a single journalnote using the SAME id and date 
                   as the first text. If the second text starts with a list of new journalnotes, return a new 
                   list of journalnotes with new (incremented) ids and dates. Repeat this for any 
                   remaining text in the document. If the first text is empty, consider the second text as a new 
                   list of journalnotes. 

                   Below is an example of what the beginning of a journalnote looks like:
                   ---
                   Hentet af: (Dataproces) Robot MinSag - Hentet den: 17.10.2024 13:22 Jobcenter Rødovre

                   # Journalnotat

                   Angående: <FIRST NAME> <LAST NAME> (010170XXXX)
                    
                   Type: 022.250.000

                   Hændelsesdato: 04.01.2024 09:50

                   Oprettet af: <FIRST NAME> <LAST NAME>

                   Oprettet den: 04.01.2024 09:50

                   ...
                   ---
                """ 
            )
        },
        {"role": "user", "content": user_prompt}
    ],
    response_model=JournalNotater,
)

    for note in journalnotes.notes:
        md_path = output_path / Path(f"{note.date}_{note.id}").with_suffix(".md")
        with md_path.open('w', encoding='utf-8') as file:
            print(f"Writing note {note.id} to {md_path}\n")
            file.write(note.text)
    
    last_note = journalnotes.notes[-1] if journalnotes.notes else JournalNotat(text="", date="No date found", id=0)
    return last_note.text, last_note.id, last_note.date


def parse_date(file_path: Path) -> datetime:
    try: 
        file_name = file_path.stem 
        date_str = file_name.split('_')[0]  
        format = "%Y-%m-%d"
        date = datetime.strptime(date_str, format)
        return date
    except Exception:
        return datetime.now()


def merge_journalnotes_chronologically(input_path_markdown: Path, input_path_pdf: Path, output_path: Path, output_filename_pdf: str):
    """
    Merges PDF pages chronologically based on dates in markdown filenames and page tokens in markdown content.
    
    Args:
        input_path_markdown: Path to directory containing markdown files with dates in filenames
        input_path_pdf: Path to the source PDF file
        output_path: Directory where the merged PDF will be saved
        output_filename_pdf: Name of the output PDF file
    """

    output_path.mkdir(exist_ok=True, parents=True)
    
    markdown_files = [f for f in input_path_markdown.iterdir() if f.is_file() and f.suffix == '.md']
    sorted_files = sorted(markdown_files, key=parse_date)
    
    if not sorted_files:
        print("No markdown files found to process")
        return
    
    reader = PdfReader(str(input_path_pdf))
    writer = PdfWriter()
    
    processed_pages = set()  # Track pages to avoid duplicates
    
    for file_path in sorted_files:
        print(f"Processing {file_path.name}")
        
        try:
            markdown_content = file_path.read_text(encoding="utf-8")
            
            page_numbers = re.findall(r'<--PAGE_NUMBER\s+(\d+)-->', markdown_content)
            page_numbers = [int(page) for page in page_numbers]
            
            if not page_numbers:
                print(f"No page numbers found in {file_path.name}")
                continue
            
           
            for page_num in page_numbers:
                page_index = page_num - 1
                
                if 0 <= page_index < len(reader.pages) and page_index not in processed_pages:
                    writer.add_page(reader.pages[page_index])
                    processed_pages.add(page_index)
                    print(f"Added page {page_num}")
                elif page_index in processed_pages:
                    print(f"Skipping page {page_num} (already processed)")
                else:
                    print(f"Warning: Page {page_num} is out of range")
                    
        except Exception as e:
            print(f"Error processing {file_path.name}: {e}")
            continue

    output_pdf_path = output_path / output_filename_pdf
    try:
        with open(output_pdf_path, "wb") as output_file:
            writer.write(output_file)
        print(f"Merged PDF saved to {output_pdf_path}")
        print(f"Total pages in merged PDF: {len(writer.pages)}")
    except Exception as e:
        print(f"Error writing merged PDF: {e}")


def split_document_by_journalnote(llm_service: LLMService, file_path_md: Path, output_path: Path):
    """
    Splits a markdown document into separate journalnotater.
    Args:
        llm_service (LLMService): The LLM service to use for processing.
        file_path_md (Path): The path to the markdown file to process.
        output_path (Path): The directory where the journalnotater will be saved.
    """
    output_path.mkdir(exist_ok=True)
    markdown_text: str = file_path_md.read_text(encoding="utf-8")

    first_text = "None"
    first_text_id = "None"
    first_text_date = "None"

    chars_to_process = len(markdown_text)

    for i in range(0, chars_to_process, 10000):
        print(f"Processing chunk {i // 10000 + 1} of {chars_to_process // 10000 + 1}")
        first_text, first_text_id, first_text_date = get_journalnotat(llm_service=llm_service,
                    first_text=first_text,
                    first_text_id=first_text_id,
                    first_text_date=first_text_date,
                    second_text=markdown_text[i: i + 10000],
                    model="gpt-4o",
                    output_path=output_path
                )



if __name__ == "__main__":

    # EXAMPLE USAGE
    file_path_markdown = Path("C:\\Users\\MagnusDiamant\\OneDrive - Howden Danmark\\Dokumenter\\AI\\rag-for-arbejdsmarkedet-arhversforsikring\\.data\\2024-0011365 -  202200925 RØD - 30% midlertidigt erhvervsevnetab (EET) - Anke - JHE\\56151a2ba999b45b596dcc991be798800d378a5016440152f7977cc4cc4bf021\\markdown\\037.03 - IND - Kommunal journal  Kommunal journal.md")

    from src.clients.openai_client import OpenAIClient
    open_ai_client = OpenAIClient(model="gpt-4o")

    llm_service = LLMService(client=open_ai_client)

    output_path = file_path_markdown.parent.parent / "journalnotater"

    split_document_by_journalnote(llm_service=llm_service, file_path_md=file_path_markdown, output_path=output_path)


    input_path_md = "C:\\Users\\MagnusDiamant\\OneDrive - Howden Danmark\\Dokumenter\\AI\\rag-for-arbejdsmarkedet-arhversforsikring\\.data\\2024-0011365 -  202200925 RØD - 30% midlertidigt erhvervsevnetab (EET) - Anke - JHE\\56151a2ba999b45b596dcc991be798800d378a5016440152f7977cc4cc4bf021\\journalnotater"

    input_path_pdf = "C:\\Users\\MagnusDiamant\\OneDrive - Howden Danmark\\Dokumenter\\AI\\rag-for-arbejdsmarkedet-arhversforsikring\\.data\\2024-0011365 -  202200925 RØD - 30% midlertidigt erhvervsevnetab (EET) - Anke - JHE\\56151a2ba999b45b596dcc991be798800d378a5016440152f7977cc4cc4bf021\\landing\\037.03 - IND - Kommunal journal  Kommunal journal.pdf"

    output_path = "C:\\Users\\MagnusDiamant\\OneDrive - Howden Danmark\\Dokumenter\\AI\\rag-for-arbejdsmarkedet-arhversforsikring\\.data\\2024-0011365 -  202200925 RØD - 30% midlertidigt erhvervsevnetab (EET) - Anke - JHE\\56151a2ba999b45b596dcc991be798800d378a5016440152f7977cc4cc4bf021\\chronological_journalnotes"

    output_filename_pdf = "merged_journalnotes.pdf"

    input_path_md = Path(input_path_md)
    input_path_pdf = Path(input_path_pdf)
    output_path = Path(output_path)

    merge_journalnotes_chronologically(
        input_path_markdown=input_path_md,
        input_path_pdf=input_path_pdf,
        output_path=output_path,
        output_filename_pdf=output_filename_pdf
    )
