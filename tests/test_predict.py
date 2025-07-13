from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient
from langdetect import LangDetectException

from app.main import app
from app.pipelines.types import PipelineType

client = TestClient(app)


class TestPredict:
    @pytest.fixture(autouse=True)
    def setup_client(self):
        self.client = client

    def test_predict_valid_input(self):
        payload = {
            "text": "I love programming!",
            "pipeline": PipelineType.base_multilingual_uncased_sentiment,
        }
        response = self.client.post("/predict", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "sentiment" in data
        assert "confidence" in data
        assert "language" in data
        assert isinstance(data["sentiment"], str)
        assert isinstance(data["confidence"], float)
        assert isinstance(data["language"], str)

    def test_predict_invalid_pipeline(self):
        payload = {"text": "I love programming!", "pipeline": "invalid_pipeline"}
        response = self.client.post("/predict", json=payload)
        assert response.status_code == 422

    def test_predict_non_english_text(self):
        payload = {
            "text": "Me encanta programar!",
            "pipeline": PipelineType.base_multilingual_uncased_sentiment,
        }
        response = self.client.post("/predict", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert "sentiment" in data
        assert "confidence" in data
        assert "language" in data
        assert data["language"] is not None

    def test_predict_with_language_detection_failure(self):
        payload = {
            "text": "",
            "pipeline": PipelineType.base_multilingual_uncased_sentiment,
        }
        with patch("langdetect.detect", side_effect=LangDetectException):
            response = self.client.post("/predict", json=payload)
            assert response.status_code == 200
            data = response.json()
            assert data["language"] is None
            assert "sentiment" in data
            assert "confidence" in data

    def test_predict_with_non_english_text_and_pipeline(self):
        payload = {
            "text": "Me encanta programar!",
            "pipeline": PipelineType.distilbert_base_uncased_finetuned_sst2_english,
        }
        response = self.client.post("/predict", json=payload)
        assert response.status_code == 400
        data = response.json()
        assert "detail" in data
        assert (
            data["detail"]
            == "Text is not in English. Use the multilingual model for non-English text."
        )
