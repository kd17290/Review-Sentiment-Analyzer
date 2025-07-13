from fastapi import HTTPException
from transformers import pipeline

from app.pipelines.base_pipeline import BasePipeline
from app.pipelines.types import Prediction

pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english",
)


class DistilBertBaseUncasedFineTunedSst2English(BasePipeline):
    """
    DistilBERT model fine-tuned on the SST-2 dataset for sentiment analysis.
    This model predicts sentiment for English text and returns the sentiment label
    and confidence score.
    """

    def predict(self, text: str, language: str | None = None) -> Prediction:
        """
        Predict sentiment for the given text using DistilBERT.

        :param text: The input text for sentiment analysis.
        :return: A dictionary containing sentiment and confidence.
        """
        if language and language != "en":
            # If the text is not in English, we can still use DistilBERT,
            # but it may not perform well. Consider using a multilingual model.
            raise HTTPException(
                status_code=400,
                detail="Text is not in English. Use the multilingual "
                "model for non-English text.",
            )
        result = pipeline(text)[0]
        sentiment = result["label"].lower()  # 'POSITIVE' -> 'positive'
        confidence = round(result["score"], 2)
        return Prediction(
            sentiment=sentiment,
            confidence=confidence,
        )
