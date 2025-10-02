from pydantic import BaseModel


class IRFCLOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    sector: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
