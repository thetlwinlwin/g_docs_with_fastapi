from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.oauth2 import service_account
from googleapiclient.discovery import build

from fetch_note.settings import my_setting
from fetch_note.text_extract import read_structural_elements

app = FastAPI()


origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


def get_note() -> str:
    info = my_setting.dict(exclude={"doc_id"})
    creds = service_account.Credentials.from_service_account_info(info)
    service = build(
        "docs",
        "v1",
        credentials=creds,
    )
    # pylint: disable=maybe-no-member
    document = service.documents().get(documentId=my_setting.doc_id).execute()
    doc_content = document.get("body").get("content")
    return read_structural_elements(doc_content)


@app.get("/")
def index():
    text = get_note()
    return {"x": f"{text}"}
