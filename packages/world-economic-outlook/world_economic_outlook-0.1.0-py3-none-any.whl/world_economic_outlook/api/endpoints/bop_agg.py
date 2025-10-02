from ..base import BaseAPI
from ...models.bop_agg_options import BOP_AGGOptions


class BOP_AGGAPI(BaseAPI):
    def build_endpoint(self, options: BOP_AGGOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"BOP_AGG/{join_or_star(options.country)}.{join_or_star(options.indicator)}.{join_or_star(options.type_of_transformation)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: BOP_AGGOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
