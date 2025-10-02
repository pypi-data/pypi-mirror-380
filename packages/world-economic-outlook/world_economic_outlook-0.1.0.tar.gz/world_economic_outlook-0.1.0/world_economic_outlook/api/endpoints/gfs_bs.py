from ..base import BaseAPI
from ...models.gfs_bs_options import GFS_BSOptions


class GFS_BSAPI(BaseAPI):
    def build_endpoint(self, options: GFS_BSOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"GFS_BS/{join_or_star(options.country)}.{join_or_star(options.sector)}.{join_or_star(options.gfs_grp)}.{join_or_star(options.indicator)}.{join_or_star(options.type_of_transformation)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: GFS_BSOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
