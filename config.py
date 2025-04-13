import os
from dotenv import load_dotenv

# Charger les variables d’environnement depuis le fichier .env
load_dotenv()

# === GROQ ===
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# === TWILIO ===
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
RECIPIENT_WHATSAPP_NUMBER = os.getenv("RECIPIENT_WHATSAPP_NUMBER")
