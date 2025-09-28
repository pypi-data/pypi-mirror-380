from decimal import Decimal

from pydantic import BaseModel, Field
from pydantic_extra_types.currency_code import Currency


fixed_field = Field(max_digits=5, decimal_places=2, ge=0.0, default=0.0)
percentage_field = Field(max_digits=4, decimal_places=3, ge=0.0, default=0.0)


class Fringe(BaseModel):
    fixed: Decimal = fixed_field
    percentage: Decimal = percentage_field


class Wage(BaseModel):
    currency: Currency = 'USD'
    rate: Decimal = fixed_field
    fringe: Fringe = Fringe()
