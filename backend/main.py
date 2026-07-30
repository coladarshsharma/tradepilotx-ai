from fastapi import FastAPI

app = FastAPI(
    title="TradePilotX AI",
    version="1.0.0",
    description="AI Powered Trading Intelligence Platform"
)

@app.get("/")
def home():
    return {
        "status": "running",
        "platform": "TradePilotX AI",
        "version": "1.0.0",
        "message": "Welcome to TradePilotX AI Backend"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }