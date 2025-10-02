from pydantic import BaseModel


class FSICOptions(BaseModel):
    country: str = "*"
    sector: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
