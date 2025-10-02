from pydantic import BaseModel


class CPIOptions(BaseModel):
    country: str = "*"
    index_type: str = "*"
    coicop_1999: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
