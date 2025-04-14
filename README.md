# Bot WhatsApp

![Docker CI](https://github.com/tititaya/whatsappbot-ia/actions/workflows/docker-ci.yml/badge.svg)

Ce bot envoie automatiquement des messages WhatsApp à des horaires définis, générés par une intelligence artificielle (Groq), et transmis via l'API Twilio.

---

## Fonctionnalités

- Génération intelligente de messages avec l'API **Groq**  
- Envoi automatisé de messages WhatsApp via **Twilio**  
- Planification de l'envoi via la librairie Python `schedule`  
- Pipeline CI/CD complet avec **GitHub Actions** et **Docker**  
- Tests intégrés pour valider le bon fonctionnement du bot (`test_bot.py`)

---

## Ressources utiles

- [Documentation Twilio WhatsApp API](https://www.twilio.com/docs/whatsapp)  
- [Documentation de l'API Groq](https://console.groq.com/docs/api)  
- [Documentation Docker](https://docs.docker.com/get-started/)  
- [Documentation GitHub Actions](https://docs.github.com/en/actions)

> Ces ressources peuvent être utiles si vous souhaitez forker ce dépôt ou comprendre les composants techniques utilisés.

---

## Lancement local

```bash
# Cloner le dépôt
git clone https://github.com/tititaya/whatsappbot-ia.git
cd whatsappbot-ia

# Créer et activer un environnement virtuel
python -m venv venv
source venv/bin/activate  # ou .\venv\Scripts\activate sur Windows

# Installer les dépendances
pip install -r requirements.txt

# Lancer le bot
python main.py
