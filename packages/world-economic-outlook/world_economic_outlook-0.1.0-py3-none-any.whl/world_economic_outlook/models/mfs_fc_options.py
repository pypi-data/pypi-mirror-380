from pydantic import BaseModel


class MFS_FCOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    unit: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
