from pydantic import BaseModel


class EQOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    product: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
