from abc import ABC
from abc import abstractmethod

from app.pipelines.types import Prediction


class BasePipeline(ABC):
    """
    Base model class that can be extended by other models.
    This class can include common methods or properties that all models should have.
    """

    @abstractmethod
    def predict(self, text: str, language: str | None = None) -> Prediction:
        """
        Predict sentiment for the given text.

        This method should be overridden by subclasses to provide specific
        prediction logic.

        :param text: The input text for sentiment analysis.
        :return: An instance of PredictionOut containing sentiment and confidence.
        """
        raise NotImplementedError("Subclasses should implement this method.")
