import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api import router as healthcheck_router

load_dotenv(".env")

app = FastAPI(title="App Service", version="1.0.0")

# Mount static files
app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(__file__), "static")),
    name="static",
)


# Serve the UI at root
@app.get("/", response_class=FileResponse)
def read_index():
    return os.path.join(os.path.dirname(__file__), "static", "index.html")


app.include_router(healthcheck_router)
