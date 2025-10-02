from ..base import BaseAPI
from ...models.mfs_fc_options import MFS_FCOptions


class MFS_FCAPI(BaseAPI):
    def build_endpoint(self, options: MFS_FCOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"MFS_FC/{join_or_star(options.country)}.{join_or_star(options.indicator)}.{join_or_star(options.unit)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: MFS_FCOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
