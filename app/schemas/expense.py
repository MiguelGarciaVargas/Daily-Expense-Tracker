from datetime import date, datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

# Pydantic models for request and response validation related to expenses
class ExpenseCreate(BaseModel):
    amount: Decimal = Field(gt=0)
    category: str = Field(min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=255)
    expense_date: date


class ExpenseResponse(BaseModel):
    # Configuración para permitir la creación de modelos a partir de objetos ORM
    model_config = ConfigDict(from_attributes=True)

    id: int
    amount: Decimal
    category: str
    description: str | None
    expense_date: date
    created_at: datetime
    updated_at: datetime