# server.py
# ------------------------------------------
# Ce fichier définit une petite API REST avec FastAPI.
# Il expose deux routes :
# - GET /         : Vérifie que l’API est bien en ligne
# - GET /health   : Route utilisée pour les vérifications (ex. déploiement Railway ou monitoring)
# Le serveur est lancé sur le port défini par la variable d’environnement PORT (défaut : 8080)
# ------------------------------------------

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bot WhatsApp IA actif 🚀"}

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))  # Port requis par Railway
    uvicorn.run("server:app", host="0.0.0.0", port=port)
