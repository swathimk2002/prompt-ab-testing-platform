
"""Create the main FastAPI application."""

from fastapi import FastAPI

app = FastAPI(title="Prompt A/B Testing Platform")


@app.get("/health")
def health_check():
    """Return the health status of the application."""
    return {"status": "healthy"}
