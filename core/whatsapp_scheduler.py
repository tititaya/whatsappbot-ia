# whatsapp_sender.py
# -----------------------------------------------------
# Gère l’envoi des messages WhatsApp via l’API Twilio.
# Utilise les identifiants d’authentification définis dans config.py.
# Fournit une fonction unique `send_message()` pour transmettre un message.
# -----------------------------------------------------



import time
import schedule
from core.whatsapp_prompts import generate_prompt
from core.whatsapp_groq_client import generate_message
from core.whatsapp_sender import send_message

def send_morning_message():
    prompt = generate_prompt("matin")
    message = generate_message(prompt)
    if message:
        send_message(message)

def send_evening_message():
    prompt = generate_prompt("soir")
    message = generate_message(prompt)
    if message:
        send_message(message)

def start_scheduler():
    schedule.every().day.at("08:00").do(send_morning_message)
    schedule.every().day.at("17:10").do(send_evening_message)

    print("Bot WhatsApp lancé, en attente d’envoi... (Ctrl+C pour arrêter)")
    while True:
        schedule.run_pending()
        time.sleep(60)
