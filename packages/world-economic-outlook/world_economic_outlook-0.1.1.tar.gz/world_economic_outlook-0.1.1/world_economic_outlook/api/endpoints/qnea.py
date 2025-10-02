from ..base import BaseAPI
from ...models.qnea_options import QNEAOptions


class QNEAAPI(BaseAPI):
    def build_endpoint(self, options: QNEAOptions) -> str:
        def join_or_star(val):
            if isinstance(val, list):
                return "+".join(val)
            return val or "*"

        endpoint = f"QNEA/{join_or_star(options.country)}.{join_or_star(options.indicator)}.{join_or_star(options.price_type)}.{join_or_star(options.s_adjustment)}.{join_or_star(options.type_of_transformation)}.{join_or_star(options.frequency)}"
        return endpoint

    def get_data(self, options: QNEAOptions):
        endpoint = self.build_endpoint(options)
        params = {}
        if hasattr(options, "start_date") and options.start_date not in (None, "*"):
            params["startPeriod"] = options.start_date
        if hasattr(options, "end_date") and options.end_date not in (None, "*"):
            params["endPeriod"] = options.end_date
        return self.request(endpoint, params, parse_xml=True)
