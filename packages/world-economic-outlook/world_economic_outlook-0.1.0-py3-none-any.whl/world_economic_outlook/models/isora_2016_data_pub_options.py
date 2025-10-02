from pydantic import BaseModel


class ISORA_2016_DATA_PUBOptions(BaseModel):
    jurisdiction: str = "*"
    indicator: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
