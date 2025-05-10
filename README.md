
# Outlook - API

API desenvolvida com FastAPI para envio automático de e-mails utilizando a Microsoft Graph API (Outlook).

## Tecnologias

- Python 3.10+
- FastAPI
- Microsoft Graph API
- OAuth2 Client Credentials Flow

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/thiagorosa21/Outlook-API.git
cd Outlook-Api
````

2. Crie o arquivo `.env` com suas credenciais:

```
CLIENT_ID=
CLIENT_SECRET=
TENANT_ID=
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute a API:

```bash
uvicorn main:app --reload
```

## Enviar e-mail

Faça um POST para `/send-email` com o corpo:

```json
{
  "to": "destinatario@exemplo.com",
  "subject": "Assunto do Email",
  "body": "Conteúdo do e-mail"
}
```
