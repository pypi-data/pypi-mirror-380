from pydantic import BaseModel


class MFS_NSRFOptions(BaseModel):
    country: str = "*"
    mfs_srvy: str = "*"
    indicator: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
