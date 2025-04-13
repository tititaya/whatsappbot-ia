#  Utilise une image Python légère
FROM python:3.10-slim

#  Crée le dossier de travail dans le conteneur
WORKDIR /app

#  Copie les fichiers dans le conteneur
COPY . .

#  Installe les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

#  Spécifie la commande à exécuter
CMD ["python", "main.py"]
