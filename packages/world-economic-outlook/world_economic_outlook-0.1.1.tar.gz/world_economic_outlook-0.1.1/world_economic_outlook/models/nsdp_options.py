from pydantic import BaseModel


class NSDPOptions(BaseModel):
    country: str = "*"
    nsdp_cat: str = "*"
    indicator: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
