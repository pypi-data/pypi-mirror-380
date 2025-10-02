from pydantic import BaseModel


class GDDOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
