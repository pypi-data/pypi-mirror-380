from decimal import Decimal

from pydantic import BaseModel, Field
from pydantic_extra_types.currency_code import Currency


class Fringe(BaseModel):
    fixed: Decimal = Field(max_digits=5, decimal_places=2, ge=0.0, default=0.0)
    percentage: Decimal = Field(max_digits=4, decimal_places=3, ge=0.0, default=0.0)


class Wage(BaseModel):
    currency: Currency = 'USD'
    rate: Decimal = Field(max_digits=5, decimal_places=2, ge=0.0, default=0.0)
    fringe: Fringe = Fringe()
