from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from google.oauth2 import service_account
from google.oauth2.service_account import Credentials
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


def get_service()->Credentials:
    info = my_setting.dict(exclude={"doc_id"})
    creds = service_account.Credentials.from_service_account_info(info)
    return creds
    

def get_doc_content()->str:
    my_cred = get_service()
    service = build(
        "docs",
        "v1",
        credentials=my_cred,
    )
    # pylint: disable=maybe-no-member
    document = service.documents().get(documentId=my_setting.doc_id).execute()
    doc_content = document.get("body").get("content")
    return read_structural_elements(doc_content)

def get_doc_title()->str:
    my_cred = get_service()
    service = build(
        "docs",
        "v1",
        credentials=my_cred,
    )
    # pylint: disable=maybe-no-member
    document = service.documents().get(documentId=my_setting.doc_id).execute()
    return document.get('title')


@app.get("/")
def get_content():
    content = get_doc_content()
    return {"x": f"{content}"}


@app.get('/get_title')
def get_title():
    title = get_doc_title()
    return {"Title":f"{title}"}
