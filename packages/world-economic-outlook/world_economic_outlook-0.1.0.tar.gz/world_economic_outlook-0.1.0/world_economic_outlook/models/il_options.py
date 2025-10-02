from pydantic import BaseModel


class ILOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    unit: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
