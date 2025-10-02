from pydantic import BaseModel


class PPIOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
