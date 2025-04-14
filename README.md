# Bot WhatsApp

[![Docker CI](https://github.com/tititaya/whatsappbot-ia/actions/workflows/docker.yml/badge.svg)](https://github.com/tititaya/whatsappbot-ia/actions/workflows/docker.yml)

Ce bot envoie automatiquement des messages WhatsApp aux horaires définis, générés par une IA, et envoyés via Twilio.

## Fonctionnalités

- Génération de messages via l'API Groq  
- Envoi WhatsApp via Twilio  
- Planification automatisée avec `schedule`  
- Pipeline CI/CD avec GitHub Actions + Docker

## Lancement local

```bash
python main.py
