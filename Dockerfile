# Utilise une image officielle Python
FROM python:3.10-slim

# Crée un dossier pour l’app
WORKDIR /app

# Copie les fichiers nécessaires
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Commande de démarrage
CMD ["python", "main.py"]
