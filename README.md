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

## Monitoring

Le bot dispose d'une route `/health` accessible publiquement pour vérifier qu’il est bien en ligne.

Il est recommandé d’utiliser un service comme [UptimeRobot](https://uptimerobot.com/) pour surveiller le domaine suivant :

https://whatsappbot-ia-production.up.railway.app/health

Cela permet de vérifier automatiquement que l’API est active même en cas d’inactivité prolongée.

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
