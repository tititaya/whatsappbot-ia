# server.py
# ------------------------------------------
# Ce fichier définit une petite API REST avec FastAPI.
# Il expose plusieurs routes :
# - GET /          : Vérifie que l’API est bien en ligne
# - GET /health    : Route utilisée pour le monitoring (Railway, UptimeRobot, etc.)
# - POST /webhook  : Reçoit les réponses WhatsApp et renvoie une réponse automatique selon le message
# Le serveur est lancé sur le port défini par la variable d’environnement PORT (défaut : 8080)
# ------------------------------------------

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse
import os

app = FastAPI()

@app.get("/", include_in_schema=False)
def read_root():
    return {"message": "Bot WhatsApp IA actif"}

@app.get("/health", include_in_schema=False)
@app.head("/health", include_in_schema=False)
def health_check():
    return JSONResponse(content={"status": "tkt toujour actif je ne suis pas pret a mourrir"}, status_code=200)

@app.post("/webhook", include_in_schema=False)
async def whatsapp_reply(request: Request):
    form = await request.form()
    msg = form.get("Body", "").lower()

    response = MessagingResponse()
    reply = response.message()

    if "merci" in msg:
        reply.body("Avec plaisir")
    elif "bonjour" in msg:
        reply.body("Coucou, bonne journée à toi")
    elif "tu vas bien" in msg:
        reply.body("Je vais très bien, et toi ?")
    else:
        reply.body("Merci pour ton message")

    return PlainTextResponse(str(response), media_type="application/xml")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run("server:app", host="0.0.0.0", port=port)
