from pydantic import BaseModel


class IMTSOptions(BaseModel):
    country: str = "*"
    indicator: str = "*"
    counterpart_country: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
