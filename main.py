from fastapi import FastAPI, File, UploadFile
from deepface import DeepFace
import shutil

app = FastAPI()

@app.post("/detect-gender")
async def detect_gender(file: UploadFile = File(...)):
    with open("temp.jpg", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = DeepFace.analyze(img_path="temp.jpg", actions=["gender"])
    return {
        "gender": result[0]["gender"],
        "confidence": result[0]["gender_confidence"]
    }