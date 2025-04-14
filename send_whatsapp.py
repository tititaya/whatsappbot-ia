import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
RECIPIENT_WHATSAPP_NUMBER = os.getenv("RECIPIENT_WHATSAPP_NUMBER")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_message(body: str):
    try:
        message = client.messages.create(
            from_=TWILIO_WHATSAPP_NUMBER,
            to=RECIPIENT_WHATSAPP_NUMBER,
            body=body
        )
        print(f"✅ Message envoyé : SID = {message.sid}")
    except Exception as e:
        print(f"❌ Erreur lors de l’envoi du message : {e}")
