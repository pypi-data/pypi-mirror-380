from pydantic import BaseModel


class FSICDMOptions(BaseModel):
    country: str = "*"
    sector: str = "*"
    indicator: str = "*"
    transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
