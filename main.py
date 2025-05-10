from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
TENANT_ID = os.getenv("TENANT_ID")
AUTH_URL = f"https://login.microsoftonline.com/{TENANT_ID}/oauth2/v2.0/token"

app = FastAPI()

class EmailRequest(BaseModel):
    to: str
    subject: str
    body: str

def get_access_token():
    data = {
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'https://graph.microsoft.com/.default',
        'grant_type': 'client_credentials'
    }
    response = requests.post(AUTH_URL, data=data)
    if response.status_code == 200:
        return response.json()['access_token']
    raise HTTPException(status_code=500, detail="Erro ao obter token de acesso.")

def send_email(to: str, subject: str, body: str):
    token = get_access_token()
    url = "https://graph.microsoft.com/v1.0/users/thiago.silva@vibetecnologia.com/sendMail"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "message": {
            "subject": subject,
            "body": {
                "contentType": "Text",
                "content": body
            },
            "toRecipients": [
                {
                    "emailAddress": {
                        "address": to
                    }
                }
            ]
        }
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 202:
        raise HTTPException(status_code=500, detail="Erro ao enviar e-mail.")

@app.post("/send-email")
def send(email: EmailRequest):
    send_email(email.to, email.subject, email.body)
    return {"message": "E-mail enviado com sucesso!"}
