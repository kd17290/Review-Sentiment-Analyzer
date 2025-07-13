from datetime import datetime

import pandas as pd
from fastapi import APIRouter
from langdetect import detect
from langdetect import LangDetectException

from app.pipelines.factory import PipelineFactory
from app.schema import FeedbackRequest
from app.schema import PredictionOut
from app.schema import TextIn

router = APIRouter()


@router.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@router.post("/predict", response_model=PredictionOut)
def predict(payload: TextIn):
    try:
        language = detect(payload.text)
    except LangDetectException:
        language = None
    pipeline = PipelineFactory.get_pipeline(payload.pipeline)
    prediction = pipeline.predict(payload.text, language)
    return {
        "sentiment": prediction.sentiment,
        "confidence": prediction.confidence,
        "language": language,
    }


@router.post("/feedback")
def submit_feedback(data: FeedbackRequest):
    feedback = {
        "text": data.text,
        "pipeline": data.pipeline,
        "sentiment": data.sentiment,
        "confidence": data.confidence,
        "language": data.language,
        "corrected": data.corrected,
        "timestamp": datetime.now().isoformat(),
    }
    df = pd.DataFrame([feedback])
    file_path = "feedback.csv"
    try:
        df.to_csv(
            file_path,
            mode="a",
            header=not pd.io.common.file_exists(file_path),
            index=False,
        )
    except Exception:
        df.to_csv(file_path, mode="w", header=True, index=False)
    return {"status": "stored"}
