import urllib2
from urllib import urlencode
import simplejson as json
import sys, re
import dateutil.parser

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

class IllegalArquementException(Exception):
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
                results,
                version = None
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
            resource_type = Types.snakify_type_name(type)
            type._resource_url = _API_URL + resource_type + "/"

    @classmethod
    def _request(type, baseurl, **params):
        if 'api_key' not in params:
            if len(api_key) == 0:
                raise InvalidAPIKeyError(
                        "Invalid API Key"
                    )
            params['api_key'] = api_key
        if 'field_list' in params and params['field_list'] != None:
            if not isinstance(params['field_list'], basestring):
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
        response_raw = json.loads(urllib2.urlopen(
                baseurl+"?"+params
            ).read())
        response = type._Response(**response_raw)
        if response.status_code != 1:
            raise _EXCEPTIONS.get(response.status_code,UnknownStatusError)(
                    response.error
                )
        if 'aliases' in response.results and \
                isinstance(response.results['aliases'], basestring):
            response.results['aliases'] = response.results[
                    'aliases'
                ].split('\n')
        return response

class _SingularResource(_Resource):
    def __new__(
            type,
            id,
            all = False,
            field_list = [],
            do_not_download = False,
            **kwargs
        ):
        resource_type = kwargs.get(
                'resource_type',
                type
            )
        try:
            type_id = Types()[resource_type]['id']
        except KeyError:
            return InvalidResourceError(resource_type)
        type._ensure_resource_url()
        key = "{0:d}-{1:d}".format(type_id, id)
        obj = _cached_resources.get(key)
        if obj == None:
            obj = object.__new__(
                    type,
                    id,
                    all,
                    field_list,
                    do_not_download,
                    **kwargs
                )
            _cached_resources[key] = obj
        return obj

    def __init__(
            self,
            id,
            all = False,
            field_list = [],
            do_not_download = False,
            **kwargs
        ):
        if '_ready' not in self.__dict__:
            self._ready = True
            try:
                type_id = Types()[type(self)]['id']
            except KeyError:
                raise InvalidResourceError(
                        "Resource type '{0!s}' does not exist.".format(
                                resource_type
                            )
                    )
            self._detail_url = type(self)._resource_url + \
                    "{0:d}-{1:d}/".format(type_id, id)
            self._fields = {'id': id}
            if not do_not_download:
                if all:
                    self._fields.update(self._request_object().results)
                else:
                    self._fields.update(self._request_object(
                            field_list
                        ).results)
            if 'field_list' in kwargs:
                del kwargs['field_list']
            self._fields.update(kwargs)
        elif 'field_list' in kwargs:
            self._fields.update(self._request_object(
                    kwargs['field_list']
                ).results)


    def _request_object(self, field_list = None):
        if field_list == None:
            return type(self)._request(
                    self._detail_url,
                )
        else:
            return type(self)._request(
                    self._detail_url,
                    field_list=field_list
                )

    def __getattribute__(self, name):
        def _object_attribute(name):
            return object.__getattribute__(self, name)
        try:
            if name not in ['__dict__', '_request_object'] and \
                    name not in self.__dict__:
                if name in _object_attribute('_fields'):
                    return _object_attribute('_fields')[name]
                else:
                    self._fields.update(
                            _object_attribute('_request_object')(
                                    [name]
                                ).results
                        )
                    return _object_attribute('_fields')[name]
        except KeyError:
            pass
        return _object_attribute(name)

    def __str__(self):
        return str(unicode(self))

    def __unicode__(self):
        if 'name' in self._fields:
            return unicode(self.name.encode(
                    'ascii',
                    'backslashreplace'
                )) + u" ["+unicode(self.id)+u"]"
        else:
            return u"["+unicode(self.id)+u"]"

    def __repr__(self):
        return u"<"+unicode(type(self).__name__)+u": "+unicode(self)\
                +u">"

class _ListResource(_Resource):
    def _request_object(self, **params):
        type(self)._ensure_resource_url()
        return type(self)._request(type(self)._resource_url, **params)

    def __init__(self, init_list = None, **kwargs):
        if init_list != None:
            if len(kwargs) > 0:
                raise TypeError(
                        "If 'init_list' is given it is the only "+
                        "allowed argument"
                    )
            self._results = init_list
            self._total = len(init_list)
            self._limit = len(init_list)
        else:
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
        if start < 0 or start >= self._total or \
                stop > self._total:
            raise IndexError('Index out of range')
        if len(self._results) < stop or \
                None in self._results[start:stop:step]:
            for i in range(start, stop, 100):
                response = self._request_object(
                        limit=self._limit,
                        offset=i,
                        **self._args
                    )
                self._results[i:self._limit+i] = response.results
        if type(self._results[index]) == list:
            for i in range(start, stop, step):
                if type(self._results[i]) == dict:
                    self._parse_result(i)
        elif type(self._results[index]) == dict:
            self._parse_result(index)
        return self._results[index]

    def __iter__(self):
        for index in xrange(self._total):
            yield self[index]

    def __str__(self):
        return str(unicode(self))

    def __unicode__(self):
        if len(self) == 0:
            return u"[]"
        string = u"["
        for element in self:
            string += unicode(element)+u", "
        string = string[:-2]+u"]"
        return string

    def __repr__(self):
        if len(self) == 0:
            return unicode(type(self).__name__)+u"[]"
        string = unicode(type(self).__name__)+u"["
        for element in self:
            string += repr(element)+u","
        string = string[:-1]+u"]"
        return string

    def _parse_result(self, index):
        if type(self) != Types:
            type_dict = Types()
            if type(self) == Search:
                self._results[index] = type_dict[
                        self._results[index]['resource_type']
                    ]['singular_resource_class'](
                            do_not_download=True,
                            **self._results[index]
                        )
            else:
                self._results[index] = type_dict[type(self)][
                        'singular_resource_class'
                    ](do_not_download=True, **self._results[index])

class _SortableListResource(_ListResource):
    def __init__(self, init_list = None, sort = None, **kwargs):
        if sort != None:
            if isinstance(sort, basestring):
                if ':' not in sort:
                    sort += ":asc"
            else:
                try:
                    sort = str(sort[0])+":"+str(sort[1])
                except KeyError:
                    if 'field' not in sort:
                        raise IllegalArquementException(
                                "Argument 'sort' must contain item 'field'"
                            )
                    if 'direction' in sort:
                        sort = sort['field']+":"+str(sort['direction'])
                    else:
                        sort = sort['field']+":asc"
            kwargs['sort'] = sort
        super(_SortableListResource, self).__init__(init_list, **kwargs)

class Character(_SingularResource):
    def __getattribute__(self, name):
        value = super(Character, self).__getattribute__(name)
        if name == 'birth':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'character_enemies':
            if isinstance(value, list):
                self._fields[name] = Characters(value)
            return self._fields[name]
        elif name == 'character_friends':
            if isinstance(value, list):
                self._fields[name] = Characters(value)
            return self._fields[name]
        elif name == 'creators':
            if isinstance(value, list):
                self._fields[name] = People(value)
            return self._fields[name]
        elif name == 'date_added':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'date_last_updated':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'first_appeared_in_issue':
            if isinstance(value, dict):
                self._fields[name] = Issue(**value)
            return self._fields[name]
        elif name == 'gender':
            if isinstance(value, int):
                self._fields[name] = \
                        u'\u2642' if value == 1 else \
                        u'\u2640' if value == 2 else u'\u26a7'
            return self._fields[name]
        elif name == 'issue_credits':
            if isinstance(value, list):
                self._fields[name] = Issues(value)
            return self._fields[name]
        elif name == 'issues_died_in':
            if isinstance(value, list):
                    self._fields[name] = Issues(value)
            return self._fields[name]
        elif name == 'movies':
            if isinstance(value, list):
                    self._fields[name] = Movies(value)
            return self._fields[name]
        elif name == 'origin':
            if isinstance(value, dict):
                self._fields[name] = Origin(**value)
            elif isinstance(value, list):
                self._fields[name] = Origins(value)
            return self._fields[name]
        elif name == 'powers':
            if isinstance(value, list):
                    self._fields[name] = Powers(value)
            return self._fields[name]
        elif name == 'publisher':
            if isinstance(value, dict):
                self._fields[name] = Publisher(**value)
            elif isinstance(value, list):
                self._fields[name] = Publishers(value)
            return self._fields[name]
        elif name == 'story_arc_credits':
            if isinstance(value, list):
                self._fields[name] = StoryArcs(value)
            return self._fields[name]
        elif name == 'team_enemies':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'team_friends':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'teams':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'volume_credits':
            if isinstance(value, list):
                self._fields[name] = Volumes(value)
            return self._fields[name]
        else:
            return value

class Characters(_SortableListResource):
    pass

class Chat(_SingularResource):
    pass

class Chats(_SortableListResource):
    pass

class Concept(_SingularResource):
    def __getattribute__(self, name):
        value = super(Concept, self).__getattribute__(name)
        if name == 'date_added':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'date_last_updated':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'first_appeared_in_issue':
            if isinstance(value, dict):
                self._fields[name] = Issue(**value)
            return self._fields[name]
        elif name == 'issue_credits':
            if isinstance(value, list):
                self._fields[name] = Issues(value)
            return self._fields[name]
        elif name == 'movies':
            if isinstance(value, list):
                self._fields[name] = Movies(value)
            return self._fields[name]
        elif name == 'start_year':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = int(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'volume_credits':
            if isinstance(value, list):
                self._fields[name] = Volumes(value)
            return self._fields[name]
        else:
            return value

class Concepts(_SortableListResource):
    pass

class Issue(_SingularResource):
    def __getattribute__(self, name):
        value = super(Issue, self).__getattribute__(name)
        if name == 'character_credits':
            if isinstance(value, list):
                self._fields[name] = Characters(value)
            return self._fields[name]
        elif name == 'character_died_in':
            if isinstance(value, list):
                self._fields[name] = Characters(value)
            return self._fields[name]
        elif name == 'concept_credits':
            if isinstance(value, list):
                self._fields[name] = Concepts(value)
            return self._fields[name]
        elif name == 'cover_date':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'date_added':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'date_last_updated':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'first_appearance_characters':
            if isinstance(value, list):
                self._fields[name] = Characters(value)
            return self._fields[name]
        elif name == 'first_appearance_objects':
            if isinstance(value, list):
                self._fields[name] = Objects(value)
            return self._fields[name]
        elif name == 'first_appearance_storyarcs':
            if isinstance(value, list):
                self._fields[name] = StoryArcs(value)
            return self._fields[name]
        elif name == 'first_appearance_teams':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'issue_number':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = int(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'location_credits':
            if isinstance(value, list):
                self._fields[name] = Locations(value)
            return self._fields[name]
        elif name == 'object_credits':
            if isinstance(value, list):
                self._fields[name] = Objects(value)
            return self._fields[name]
        elif name == 'person_credits':
            if isinstance(value, list):
                self._fields[name] = People(value)
            return self._fields[name]
        elif name == 'store_date':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'story_arc_credits':
            if isinstance(value, list):
                self._fields[name] = StoryArcs(value)
            return self._fields[name]
        elif name == 'team_credits':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'team_disbanded_in':
            if isinstance(value, list):
                self._fields[name] = Teams(value)
            return self._fields[name]
        elif name == 'volume':
            if isinstance(value, dict):
                self._fields[name] = Volume(**value)
            return self._fields[name]
        else:
            return value

    def __unicode__(self):
        string = u""
        if 'name' in self._fields and self._fields['name'] != None:
            string += unicode(self.name.encode(
                        'ascii',
                        'backslashreplace'
                    ))+u" "
            if 'issue_number' in self._fields:
                string += u"#"+unicode(self.issue_number)+u" "
        else:
            if 'issue_number' in self._fields:
                string += u"#"+unicode(self.issue_number)+u" "
            if 'volume' in self._fields:
                string = unicode(self.volume.name.encode(
                        'ascii',
                        'backslashreplace'
                    ))+u" "+string
        return string + u"["+unicode(self.id)+u"]"

class Issues(_SortableListResource):
    pass

class Location(_SingularResource):
    def __getattribute__(self, name):
        value = super(Location, self).__getattribute__(name)
        if name == 'date_added':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'date_last_updated':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = dateutil.parser.parse(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'first_appeared_in_issue':
            if isinstance(value, dict):
                self._fields[name] = Issue(**value)
            return self._fields[name]
        elif name == 'issue_credits':
            if isinstance(value, list):
                self._fields[name] = Issues(value)
            return self._fields[name]
        elif name == 'movies':
            if isinstance(value, list):
                self._fields[name] = Movies(value)
            return self._fields[name]
        elif name == 'start_year':
            if isinstance(value, basestring):
                try:
                    self._fields[name] = int(value)
                except ValueError:
                    pass
            return self._fields[name]
        elif name == 'story_arc_credits':
            if isinstance(value, list):
                self._fields[name] = StoryArcs(value)
            return self._fields[name]
        elif name == 'volume_credits':
            if isinstance(value, list):
                self._fields[name] = Volumes(value)
            return self._fields[name]
        else:
            return value

class Locations(_SortableListResource):
    pass

class Movie(_SingularResource):
    pass

class Movies(_SortableListResource):
    pass

class Object(_SingularResource):
    pass

class Objects(_SortableListResource):
    pass

class Origin(_SingularResource):
    pass

class Origins(_SortableListResource):
    pass

class Person(_SingularResource):
    pass

class People(_SortableListResource):
    pass

class Power(_SingularResource):
    pass

class Powers(_SortableListResource):
    pass

class Promo(_SingularResource):
    pass

class Promos(_SortableListResource):
    pass

class Publisher(_SingularResource):
    pass

class Publishers(_SortableListResource):
    pass

class Search(_ListResource):
    def __init__(self, resources, query, **kwargs):
        super(Search, self).__init__(
                resources=resources,
                query=query,
                **kwargs
            )

class StoryArc(_SingularResource):
    pass

class StoryArcs(_SortableListResource):
    pass

class Team(_SingularResource):
    pass

class Teams(_SortableListResource):
    pass

class Types(_ListResource):
    def __new__(type):
        if not '_instance' in type.__dict__:
            type._instance = object.__new__(type)
        return type._instance

    def __init__(self):
        if not '_ready' in dir(self):
            super(Types, self).__init__()
            self._mapping = {}
            for type in self:
                type['singular_resource_class'] = getattr(
                        sys.modules[__name__],
                        Types._camilify_type_name(
                                type['detail_resource_name']
                            )
                    )
                self._mapping[type['detail_resource_name']] = type
                self._mapping[type['list_resource_name']] = type
            self._ready = True

    def __getitem__(self, key):
        if isinstance(key, (int, long, slice)):
            return super(Types, self).__getitem__(key)
        if isinstance(key, type):
            return self._mapping[self.snakify_type_name(key)]
        return self._mapping[key]

    @staticmethod
    def snakify_type_name(type):
        return re.sub(r'([A-Z]+)',r"_\1", type.__name__)[1:].lower()

    @staticmethod
    def _camilify_type_name(string):
        string = string[0].upper() + string[1:].lower()
        camel_string = ""
        next_upper = False
        for c in string:
            if c == "_":
                next_upper = True
                continue
            if next_upper:
                camel_string += c.upper()
                next_upper = False
            else:
                camel_string += c
        return camel_string

class Video(_SingularResource):
    pass

class Videos(_SortableListResource):
    pass

class VideoType(_SingularResource):
    pass

class VideoTypes(_SortableListResource):
    pass

class Volume(_SingularResource):
    pass

class Volumes(_SortableListResource):
    pass
