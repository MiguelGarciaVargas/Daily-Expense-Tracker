from fastapi import FastAPI

from app.api.health import router as health_router

app = FastAPI(
    title="Daily Expense Tracker API",
    description="API for tracking daily expenses and summaries.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Daily Expense Tracker API!"}

app.include_router(health_router)