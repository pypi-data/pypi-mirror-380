from pydantic import BaseModel


class PIOptions(BaseModel):
    country: str = "*"
    production_index: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
