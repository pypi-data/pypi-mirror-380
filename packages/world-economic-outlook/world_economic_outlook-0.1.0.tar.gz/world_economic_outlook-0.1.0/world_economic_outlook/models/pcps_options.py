from pydantic import BaseModel


class PCPSOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    data_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
