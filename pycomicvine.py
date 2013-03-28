import urllib2
from urllib import urlencode
import simplejson as json
import sys

_API_URL = "https://www.comicvine.com/api/"

_cached_resources = {}

api_key = ""

class InvalidResourceError(Exception):
    pass

class InvalidAPIKeyError(Exception):
    pass

class ObjectNotFoundError(Exception):
    pass

class ErrorInURLFormatError(Exception):
    pass

class JSONError(Exception):
    pass

class FilterError(Exception):
    pass

class SubscriberOnlyError(Exception):
    pass

class UnknownStatusError(Exception):
    pass

_EXCEPTIONS = {
        100: InvalidAPIKeyError,
        101: ObjectNotFoundError,
        102: ErrorInURLFormatError,
        103: JSONError,
        104: FilterError,
        105: SubscriberOnlyError,
    }

class _Resource(object):
    class _Response:
        def __init__(
                self, 
                error, 
                limit, 
                offset, 
                number_of_page_results,
                number_of_total_results,
                status_code,
                version,
                results
            ):
            self.error = error
            self.limit = limit
            self.offset = offset
            self.number_of_page_results = number_of_page_results
            self.number_of_total_results = number_of_total_results 
            self.status_code = status_code
            self.results = results
    
    def __init__(self, *args, **kwargs):
        raise NotImplemented()

    def _request_object(self, baseurl, **params):
        raise NotImplemented()

    @classmethod
    def _ensure_resource_url(type):
        if not '_resource_url' in type.__dict__:
            resource_type = type.__name__.lower()
            type._resource_url = _API_URL + resource_type + "/"

    @classmethod
    def _request(type, baseurl, **params):
        if 'api_key' not in params:
            if len(api_key) == 0:
                raise InvalidAPIKeyError(
                        "Invalid API Key"    
                    )
            params['api_key'] = api_key 
        params['format'] = 'json'
        params = urlencode(params)
        response = type._Response(**json.loads(urllib2.urlopen(
                baseurl+"?"+params
            ).read()))
        if response.status_code != 1:
            raise _EXCEPTIONS.get(response.status_code,UnknownStatusError)(
                    response.error
                )
        return response

