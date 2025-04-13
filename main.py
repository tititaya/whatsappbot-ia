import time
import schedule
from send_whatsapp import send_message

# Planifie le message du matin
schedule.every().day.at("08:00").do(lambda: send_message("matin"))

# Planifie le message du soir
schedule.every().day.at("16:01").do(lambda: send_message("soir"))

print("⏳ Bot WhatsApp en attente... (Ctrl+C pour arrêter)")

while True:
    schedule.run_pending()
    time.sleep(60)
