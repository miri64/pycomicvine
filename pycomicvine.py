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
        if 'field_list' in params:
            if not isinstance(params['field_list'], (str, unicode)):
                field_list = ""
                try:
                    for field_name in params['field_list']:
                        field_list += str(field_name)+","
                except TypeError, e:
                    raise IllegalArquementException(
                            "'field_list' must be iterable"
                        )
                params['field_list'] = field_list
            if re.search(
                    "([a-z_]*,)*id(,[a-z_]*)*", params['field_list']
                ) == None:
                params['field_list'] = "id," + params['field_list']
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

class _ListResource(_Resource):
    def _request_object(self, **params):
        type(self)._ensure_resource_url()
        return type(self)._request(type(self)._resource_url, **params)

    def __init__(self, **kwargs):
        response = self._request_object(**kwargs)
        self._results = response.offset*[None] + response.results
        self._total = response.number_of_total_results
        self._limit = response.limit
        if 'limit' in kwargs:
            del kwargs['limit']
        if 'offset' in kwargs:
            del kwargs['offset']
        self._args = kwargs

    def __len__(self):
        return self._total

    def __getitem__(self, index):
        if type(index) == slice:
            start = index.start or 0
            stop = index.stop or self._total
            step = index.step or 1
        else:
            start = index
            stop = index+1
            step = 1
        if start < 0 or start >= self._total or stop < 0 or \
                stop > self._total:
            raise IndexError['Index out of range']
        if len(self._results) < stop or \
                None in self._results[start:stop:step]:
            for i in range(start, stop, 100):
                response = self._request_object(
                        limit=self._limit,
                        offset=i,
                        **self._args
                    )
                self._results[i:self._limit+i] = response.results
        return self._results[index]

    def __iter__(self):
        for index in xrange(self._total):
            yield self[index]
