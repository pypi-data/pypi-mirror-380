from src.services.llm_service import LLMService


def determine_date_from_content(llm_service: LLMService, data, model) -> str:

    user_prompt = f"{data}"
    response = llm_service.get_response(
        messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an expert document analyst.\n"
                            "Given the following document text, extract only the document’s creation date.\n"
                            "Normally this be given in the top of the document"
                            "if the data is an email take the date in the header"
                            "If the document contains labels such as Udskriftdato, Indsendelsestidspunkt, Print Date, Creation Date, or similar phrases followed by a date, treat that date as the document’s creation date."
                            "if the document is a journal look for labels as Udskrevet, Hentet den or similar phrases followed by a date, treat that date as the document’s creation date.\n"
                            "There may be many dates in the document (such as deadlines, revision dates, signatures, or references), "
                            "but you must identify and return only the date that indicates when the document was first created or issued.\n"
                            "Return the date in YYYY-MM-DD format.\n"
                            "If no clear creation date can be found, respond with \"No creation date found.\"\n\n"
                        )
                    },
                    {"role": "user", "content": user_prompt}
            ],
            model=model,
        )

    return response.choices[0].message.content.strip()