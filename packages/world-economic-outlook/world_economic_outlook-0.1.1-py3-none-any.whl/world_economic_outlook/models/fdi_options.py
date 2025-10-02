from pydantic import BaseModel


class FDIOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
