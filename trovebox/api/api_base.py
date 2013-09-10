"""
api_base.py: Base class for all API classes
"""

class ApiBase(object):
    """ Base class for all API objects """
    def __init__(self, client):
        self._client = client

    @staticmethod
    def _build_filter_string(filters):
        """
        :param filters: dictionary containing the filters
        :returns: filter_string formatted for an API endpoint
        """
        filter_string = ""
        if filters is not None:
            for filt in filters:
                filter_string += "%s-%s/" % (filt, filters[filt])
        return filter_string

    @staticmethod
    def _extract_id(obj):
        """ Return obj.id, or obj if the object doesn't have an ID """
        try:
            return obj.id
        except AttributeError:
            return obj

    @staticmethod
    def _result_to_list(result):
        """ Handle the case where the result contains no items """
        if not result:
            return []
        if "totalRows" in result[0] and result[0]["totalRows"] == 0:
            return []
        else:
            return result
