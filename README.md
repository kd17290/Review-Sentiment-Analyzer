# Sentiment Analysis
This is a simple sentiment analysis application using Python, FastAPI, and Hugging Face Transformers.

# Requirements
- Python 3.13
- docker
- FastAPI
- Hugging Face Transformers
- Uvicorn
- Pydantic

# Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:kd17290/Review-Sentiment-Analyzer.git
2. Change into the project directory:
   ```bash
   cd sentiment-analysis
   ```
3. Install the required packages:
   ```bash
   make build
   ```
4. Start the FastAPI server:
   ```bash
    make up
    ```
5. Open your browser and go to `http://localhost:8001/docs` to access the API documentation.
6. You can test the API by sending a POST request to `/predict` with a JSON body containing the text you want to analyze. For example:
   ```json
   {
       "text": "I love programming!"
   }
   ```

    Response
    ```json
    {
        "label": "POSITIVE",
        "score": 0.9998
    }
    ```

# Usage
You can use the API to analyze the sentiment of any text. The API will return a label indicating whether the sentiment is positive, negative, or neutral, along with a confidence score.
# Example
Example Request
```bash
curl -X POST "http://localhost:8001/predict" -H "Content-Type: application/json" -d '{"text": "I love programming!"}'
```
Example Response
```json
{
    "label": "POSITIVE",
    "score": 0.9998
}
```
# File Structure
```
sentiment-analysis/
├── app/
│   ├── pipelines/
│   │   ├── __init__.py
│   │   └── base_pipeline.py
│   │   └── base_multilingual_uncased_sentiment.py
│   │   └── distilbert_base_uncased_finetuned_sst2_english.py
│   |   └── factory.py
│   |   └── types.py
│   ├── api.py
│   ├── main.py
│   └── schema.py
├── tests
│   ├── test_health.py
│   └── test_predict.py
├── .dockerignore
├── .gitignore
├── .pre-commit-config.yaml
├── docker-compose.yml
├── Dockerfile
├── Makefile
├── poetry.lock
├── pyproject.toml
└── README.md
```

# Features
- FastAPI for building the API
- Hugging Face Transformers for sentiment analysis
- Docker support for easy deployment
- Pre-commit hooks for code quality
- Unit tests for API endpoints
- Multilingual support for sentiment analysis
- pluggable pipeline architecture for sentiment analysis models
- Factory pattern for creating sentiment analysis pipelines
- Type annotations for better code clarity
- Pydantic for data validation and serialization
- API documentation with Swagger UI
- Health check endpoint to verify the service is running
- Support for multiple sentiment analysis models
- Cached models in docker to speed up the startup time

# Supported Commands
```bash
make build          # Build the Docker image
make up             # Start the FastAPI server with Docker Compose
make down           # Stop the FastAPI server
make remove         # Remove the Docker containers and images
make tests          # Run the unit tests
make lint           # Run linters to check code quality
make install        # Install dependencies using Poetry
make lock           # Lock dependencies using Poetry
```

# License
This project is licensed under the MIT License.

# Contributing
If you want to contribute to this project, feel free to open an issue or submit a pull request. Contributions are welcome!
