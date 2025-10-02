from pydantic import BaseModel


class GFS_BSOptions(BaseModel):
    country: str = "*"
    sector: str = "*"
    gfs_grp: str = "*"
    indicator: str = "*"
    type_of_transformation: str = "*"
    frequency: str = "*"
    start_date: str = None
    end_date: str = None
