# server.py
# ------------------------------------------
# API REST avec FastAPI pour le bot WhatsApp IA
# Route GET /         : test d’activité
# Route GET /health   : monitoring pour Railway
# Route POST /webhook : réception et réponse automatique aux messages Twilio
# ------------------------------------------

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import os
import requests

app = FastAPI()

# ➤ Test simple (accueil)
@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Bot WhatsApp IA actif"}

# ➤ Monitoring Railway
@app.get("/health", include_in_schema=False)
@app.head("/health", include_in_schema=False)
def health_check():
    return JSONResponse(content={"status": "Actif"}, status_code=200)

# ➤ Réponse auto à Twilio
@app.post("/webhook", include_in_schema=False)
async def whatsapp_webhook(request: Request):
    form = await request.form()
    msg_body = form.get("Body", "").strip().lower()
    sender = form.get("From")

    print(f"Message reçu de {sender} : {msg_body}")
    print(dict(form))
    if not sender:
        return JSONResponse(content={"error": "Missing sender"}, status_code=400)

    # Liste des réponses automatiques (sans emoji)
    responses = {
        "bonjour": "Coucou à toi",
        "merci": "Avec plaisir",
        "salut": "Salut à toi",
        "tu vas bien": "Je vais très bien, et toi ?",
    }

    # Réponse correspondante
    for keyword, reply in responses.items():
        if keyword in msg_body:
            send_whatsapp_reply(to=sender, message=reply)
            break  # Ne pas répondre plusieurs fois

    return JSONResponse(content={"status": "message reçu"})

# ➤ Fonction d'envoi de réponse via Twilio
def send_whatsapp_reply(to: str, message: str):
    from_number = "whatsapp:+14155238886"  # Numéro Twilio Sandbox
    TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
    TWILIO_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")

    if not TWILIO_SID or not TWILIO_TOKEN:
        print("Identifiants Twilio manquants !")
        return

    url = f"https://api.twilio.com/2010-04-01/Accounts/{TWILIO_SID}/Messages.json"

    data = {
        "From": from_number,
        "To": to,
        "Body": message
    }

    print(f"Envoi de la réponse à {to} : {message}")

    response = requests.post(url, data=data, auth=(TWILIO_SID, TWILIO_TOKEN))

    if response.status_code != 201:
        print("Erreur lors de l’envoi :", response.text)
