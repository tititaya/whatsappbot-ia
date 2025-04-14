# Bot WhatsApp

![Docker CI](https://github.com/tititaya/whatsappbot-ia/actions/workflows/docker-ci.yml/badge.svg)

Ce bot envoie automatiquement des messages WhatsApp à des horaires définis, générés par une intelligence artificielle (Groq), et transmis via l'API Twilio.

---

##  Fonctionnalités

- **Génération intelligente de messages** avec l'API **Groq**
- **Envoi automatisé** de messages WhatsApp via **Twilio**
- **Planification** de l’envoi via la librairie Python `schedule`
- **Pipeline CI/CD** complet avec **GitHub Actions** et **Docker**
- **Tests intégrés** pour valider le bon fonctionnement du bot (`test_bot.py`)

---

##  Lancement local

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
