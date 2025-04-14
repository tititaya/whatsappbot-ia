FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier le fichier requirements.txt et installer les dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le code
COPY . .

# Commande par défaut à exécuter
CMD ["python", "main.py"]
