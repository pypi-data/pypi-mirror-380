from ..base import BaseAPI
from ...models.gfs_soo_options import GFS_SOOOptions


class GFS_SOOAPI(BaseAPI):
    def build_endpoint(self, options: GFS_SOOOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"GFS_SOO/{join_or_star(options.country)}.{join_or_star(options.sector)}.{join_or_star(options.gfs_grp)}.{join_or_star(options.indicator)}.{join_or_star(options.type_of_transformation)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: GFS_SOOOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
