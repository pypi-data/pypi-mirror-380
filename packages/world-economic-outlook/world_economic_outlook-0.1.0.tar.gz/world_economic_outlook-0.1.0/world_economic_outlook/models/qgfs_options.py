from pydantic import BaseModel


class QGFSOptions(BaseModel):
    country: str = "*"
    accounts: str = "*"
    sector: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
