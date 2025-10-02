from pydantic import BaseModel


class DIPOptions(BaseModel):
    country: str = "*"
    dv_type: str = "*"
    indicator: str = "*"
    counterpart_country: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
