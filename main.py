from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to RAG Regulatory Document Search"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

@app.get("/about")
def about():
    return {
        "project": "RAG Regulatory Document Search",
        "developer": "Devi Sri Macharla"
    }