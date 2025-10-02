from pydantic import BaseModel


class CTOTOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    wgt_type: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
