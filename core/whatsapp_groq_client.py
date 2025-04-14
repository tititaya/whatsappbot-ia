# whatsapp_groq_client.py
# -----------------------------------------------------
# Ce module envoie une requête POST à l’API Groq (LLM).
# Il génère une réponse textuelle à partir d’un prompt.
# La clé d’API est chargée depuis le fichier config.py.
# Utilise le modèle "llama3-70b-8192" pour générer les messages.
# -----------------------------------------------------



import os
import httpx
from config import GROQ_API_KEY

def generate_message(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": "Tu rédiges des messages sincères et naturels d’un père à la mère de son enfant."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = httpx.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"].strip()
        else:
            print(f"[Erreur API] Code : {response.status_code} — Réponse : {response.text}")
            return None
    except Exception as e:
        print(f"[Exception] {e}")
        return None
