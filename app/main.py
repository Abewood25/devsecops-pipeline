from fastapi import FastAPI

app = FastAPI(
    title="Secure DevSecOps API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Secure DevSecOps Pipeline",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }