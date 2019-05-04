from . import Source as BaseSource


class Source(BaseSource):
    _id = 'WB'

    def modify_request_args(self, kwargs):
        """World Bank's agency ID."""
        kwargs.setdefault('agency', 'WBG_WITS')
