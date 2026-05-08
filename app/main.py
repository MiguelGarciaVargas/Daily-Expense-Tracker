from fastapi import FastAPI

from app.database import Base, engine
from app.models import expense

from app.api.health import router as health_router
from app.api.expenses import router as expenses_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Daily Expense Tracker API",
    description="API for tracking daily expenses and summaries.",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"message": "Welcome to the Daily Expense Tracker API!"}

app.include_router(health_router)
app.include_router(expenses_router )