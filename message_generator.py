from datetime import datetime
import os
import httpx
from dotenv import load_dotenv
import random

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

greetings_morning = [
    "Bonjour Vanoushka",
    "Coucou Vanoushka",
    "Salut Vanoushka",
    "Hello Vanoushka",
    "Bonne matinée Vanoushka"
]

greetings_evening = [
    "Bonsoir Vanoushka",
    "Bonne soirée Vanoushka",
    "Salut ce soir Vanoushka",
    "Hey Vanoushka",
    "J’espère que ta soirée se passe bien Vanoushka"
]

questions_about_nael = [
    "Comment Naël se porte aujourd’hui ?",
    "Est-ce que Naël mange bien en ce moment ?",
    "Comment se passe son sommeil ces derniers temps ?",
    "As-tu eu un moment calme avec lui aujourd’hui ?",
    "Est-ce qu’il rigole beaucoup en ce moment ?",
    "Il découvre de nouvelles choses ces jours-ci ?",
    "Comment il se réveille en ce moment ?",
    "Tu as remarqué quelque chose de nouveau chez lui ?",
    "Est-ce qu’il a vu son pédiatre récemment ?",
    "As-tu besoin de quelque chose pour Naël ?",
    "Est-ce que tout va bien côté santé avec lui ?"
]

def generate_prompt(period: str) -> str:
    date = datetime.now().strftime("%A %d %B %Y")

    greeting = random.choice(greetings_morning) if period == "matin" else random.choice(greetings_evening)
    question = random.choice(questions_about_nael)

    prompt = (
        f"Nous sommes le {date}. Rédige un message court, bienveillant et naturel d’un père à la mère de son enfant. "
        f"Le message doit commencer par : {greeting}. Il doit poser une seule question sincère sur leur enfant Naël, comme : « {question} ». "
        f"Le ton doit rester simple, respectueux, humain, sans être froid ni distant. "
        f"Ne fais aucune supposition sur ce que le père sait. Ne dis jamais qu’il a vu Naël ou qu’il connaît ce qu’il a fait. "
        f"Ne parle jamais d’amour ou de sentiments amoureux envers la mère. "
        f"Garde le message naturel, comme un vrai SMS rapide et attentionné."
    )

    return prompt

def generate_message(prompt: str):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "Tu rédiges des messages sincères et naturels d’un père à la mère de son enfant, sans exagération ni supposition."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = httpx.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            print(f"🪵 Code HTTP : {response.status_code}")
            print(f"🪵 Réponse brute : {response.text}")
            return None
    except Exception as e:
        print(f"Erreur : {e}")
        return None

# Test local
if __name__ == "__main__":
    print("☀️ Message du matin :")
    morning_prompt = generate_prompt("matin")
    morning_message = generate_message(morning_prompt)
    print(morning_message or "Erreur lors de la génération du message.")

    print("\n🌙 Message du soir :")
    evening_prompt = generate_prompt("soir")
    evening_message = generate_message(evening_prompt)
    print(evening_message or "Erreur lors de la génération du message.")
