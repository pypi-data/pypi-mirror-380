from pydantic import BaseModel


class ITG_WCAOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
