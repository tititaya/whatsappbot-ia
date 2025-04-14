import time
import schedule
from message_generator import generate_prompt, generate_message
from send_whatsapp import send_message

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

# Planifie le message du matin
schedule.every().day.at("00:58").do(send_morning_message)

# Planifie le message du soir
schedule.every().day.at("09:23").do(send_evening_message)

print("⏳ Bot WhatsApp en attente... (Ctrl+C pour arrêter)")

while True:
    schedule.run_pending()
    time.sleep(60)
