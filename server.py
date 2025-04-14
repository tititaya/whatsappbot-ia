# server.py

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Bot WhatsApp IA actif 🚀"}

@app.get("/health")
def health_check():
    return JSONResponse(content={"status": "ok"}, status_code=200)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=8080)
