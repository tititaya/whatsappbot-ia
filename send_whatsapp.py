import os
import httpx
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_prompt(period: str):
    date_str = datetime.now().strftime("%A %d %B %Y")

    prompt = (
        f"Nous sommes le {date_str}. Tu vas écrire un message court et naturel d’un père à la mère de son fils Naël, prénommée Vanoushka (ou Ossono). "
        f"Ce message doit être sincère, respectueux et tourné uniquement vers l’enfant, sans émotion déplacée ni formule d’amour. "
        f"N'invente JAMAIS d’événements. Tu ne dois PAS mentionner : "
        f"• de rendez-vous (médical, crèche, etc.) "
        f"• de souvenirs précis (visite, sortie, appel, moment passé ensemble) "
        f"• de comportement que le père n’a pas pu observer "
        f"• de faits ou d’informations non confirmés. "
        f"Tu peux poser des questions simples sur la santé, l’alimentation, ou le sommeil de Naël, ou demander s’il a passé une bonne journée. "
    )

    if period == "matin":
        prompt += (
            "Ce message est pour le matin. Il peut souhaiter une bonne journée à Vanoushka, lui dire qu’il pense à Naël dès le réveil, et poser une ou deux questions sur Naël."
        )
    else:
        prompt += (
            "Ce message est pour le soir. Il peut souhaiter une soirée douce, dire qu’il espère que Naël a passé une bonne journée, et proposer son aide si besoin."
        )

    prompt += (
        " Tu n’utiliseras jamais le prénom du père. Évite les messages trop longs. Le ton doit rester humain, familier, attentionné, jamais formel."
    )

    return prompt


if __name__ == "__main__":
    print("☀️ Message du matin :")
    morning_prompt = generate_prompt("matin")
    morning_message = generate_message(morning_prompt)
    print(morning_message or "Erreur lors de la génération du message.")

    print("\n🌙 Message du soir :")
    evening_prompt = generate_prompt("soir")
    evening_message = generate_message(evening_prompt)
    print(evening_message or "Erreur lors de la génération du message.")
