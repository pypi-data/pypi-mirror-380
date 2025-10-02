from pydantic import BaseModel


class MFS_MAOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    unit: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
