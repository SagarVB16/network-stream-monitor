from fastapi import FastAPI

app = FastAPI(
    title="IP Network Stream Monitor",
    description="Real-time packet monitoring and fault detection system",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "IP Network Stream Monitor Backend Active"
    }


@app.get("/health")
def health_check():
    return {
        "server": "healthy"
    }