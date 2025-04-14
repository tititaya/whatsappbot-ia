# Utiliser une image Python légère
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier tous les fichiers dans le conteneur
COPY . .

# Exposer le port utilisé par Flask
EXPOSE 8080

# Lancer l'API Flask pour le /health-check
CMD ["python", "server.py"]
