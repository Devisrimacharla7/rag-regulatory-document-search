from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "status": "uploaded successfully"
    }