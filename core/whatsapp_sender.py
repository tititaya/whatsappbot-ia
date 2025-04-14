# whatsapp_sender.py
# -----------------------------------------------------
# Gère l’envoi des messages WhatsApp via l’API Twilio.
# Utilise les identifiants d’authentification définis dans config.py.
# Fournit une fonction unique `send_message()` pour transmettre un message.
# -----------------------------------------------------


import os
from dotenv import load_dotenv
from twilio.rest import Client
from config import TWILIO_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER, RECIPIENT_WHATSAPP_NUMBER

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_message(body: str):
    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=RECIPIENT_WHATSAPP_NUMBER,
            body=body
        )
        print(f"Message WhatsApp envoyé : SID = {message.sid}")
    except Exception as e:
        print(f"Erreur lors de l’envoi du message WhatsApp : {e}")
