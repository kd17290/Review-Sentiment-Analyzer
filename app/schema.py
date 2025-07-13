from pydantic import BaseModel

from app.pipelines.types import PipelineType


class TextIn(BaseModel):
    text: str
    pipeline: PipelineType


class PredictionOut(BaseModel):
    sentiment: str
    confidence: float
    language: str | None


class FeedbackRequest(BaseModel):
    text: str
    pipeline: PipelineType
    sentiment: str
    confidence: float
    language: str | None
    corrected: str
