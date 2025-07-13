from enum import Enum

from pydantic import BaseModel


class PipelineType(str, Enum):
    base_multilingual_uncased_sentiment = "base_multilingual_uncased_sentiment"
    distilbert_base_uncased_finetuned_sst2_english = (
        "distilbert_base_uncased_finetuned_sst2_english"
    )


class Prediction(BaseModel):
    sentiment: str
    confidence: float
