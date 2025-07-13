from transformers import pipeline

from app.pipelines.base_pipeline import BasePipeline
from app.pipelines.types import Prediction

pipeline = pipeline(
    "sentiment-analysis",
    model="nlptown/bert-base-multilingual-uncased-sentiment",
)


class NlptownBertBaseMultilingualUncasedSentiment(BasePipeline):
    """
    A class representing a multilingual sentiment analysis model based on the
    Nlptown Bert Base Uncased architecture.
    This class is designed to handle sentiment analysis for multiple languages
    using a pretrained model.
    """

    def predict(self, text: str, language: str | None = None) -> Prediction:
        """
        Predict sentiment for the given text using the multilingual model.

        :param text: The input text for sentiment analysis.
        :return: A dictionary containing sentiment and confidence.
        """
        result = pipeline(text)[0]
        label = result["label"]  # e.g., '4 stars'

        # Convert star rating to polarity
        label_map = {
            "1 star": "very negative",
            "2 stars": "negative",
            "3 stars": "neutral",
            "4 stars": "positive",
            "5 stars": "very positive",
        }
        sentiment = label_map.get(label.lower(), "neutral")
        confidence = round(result["score"], 2)

        return Prediction(
            sentiment=sentiment,
            confidence=confidence,
        )
