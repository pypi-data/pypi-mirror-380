from pydantic import BaseModel


class EDOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
