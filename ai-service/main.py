from fastapi import FastAPI, UploadFile

app = FastAPI(title="AI Detection Service")

@app.get("/health")
def health():
    return {"status": "AI service running"}

@app.post("/detect")
async def detect(file: UploadFile):
    return {
        "filename": file.filename,
        "fake_score": 0.82,
        "label": "FAKE"
    }
