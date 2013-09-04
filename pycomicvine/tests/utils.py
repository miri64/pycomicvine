import logging
import random
import ssl
import unittest
import urllib2

TRIES=3
TIMEOUT=60

class TimeoutError(Exception):
    pass

def test_3times_then_fail(func, *args, **kwargs):
    log = logging.getLogger("tests")
    for i in range(TRIES):
        try:
            return func(*args, **kwargs)
        except urllib2.HTTPError, e:
            if e.code == 500:
                log.debug("Internal server error (func=%s%s, kwargs=%s, try=%d)" %
                        (repr(func), str(args), str(kwargs), i)
                    )
                if i == TRIES-1:
                    raise TimeoutError('To many HTTP-Errors')
        except ssl.SSLError, e:
            if e.msg == "The read operation timed out":
                log.debug("Timeout error (func=%s%s, kwargs=%s, try=%d)" %
                        (repr(func), str(args), str(kwargs), i)
                    )
                if i == TRIES-1:
                    raise TimeoutError('To many HTTP-Timeouts')
        except UnicodeEncodeError, e:
            log.warning("Fail because of unicode encoding error: %s",
                        e)
            if i == TRIES-1:
                raise TimeoutError('To many Unicode encoding errors')

class ListResourceTestCase(unittest.TestCase):
    def get_id_and_name_test(self, cls, test_against):
        try:
            instances = test_3times_then_fail(
                    cls,
                    field_list=['name','id'],
                    timeout=TIMEOUT
                )
            if len(instances) > 0:
                if len(instances) > 100:
                    rand_offset = random.randint(1,len(instances)-100)
                else:
                    rand_offset = 1
                max_index = random.randint(
                        rand_offset,
                        min(len(instances), rand_offset+300)
                    )
                logging.getLogger("tests").debug(
                        "%s.test_get_id_and_name: rand_offset = %d, max_index = %d",
                        type(self).__name__,
                        rand_offset,
                        max_index
                    )
                instances = test_3times_then_fail(
                        cls,
                        field_list=['name','id'],
                        limit=100,
                        offset=rand_offset,
                        timeout=TIMEOUT
                    )
                self.assertNotEqual(len(instances), 0)
                for c in test_3times_then_fail(list,instances[
                        rand_offset:max_index
                    ]):
                    self.assertIsInstance(c, test_against)
            else:
                logging.getLogger("tests").debug(
                        "%s.test_get_id_and_name: no instances => no test",
                        type(self).__name__
                    )
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)

class SingularResourceTestCase(unittest.TestCase):
    def get_random_instance(self,cls):
        self.id, self.name = None, None
        try:
            instances = test_3times_then_fail(
                    cls,
                    field_list=['id','name'],
                    timeout=TIMEOUT
                )
            if instances != None and len(instances) > 0:
                rand_instance = test_3times_then_fail(
                        random.choice,
                        instances
                    )
                self.id, self.name = rand_instance.id, \
                        rand_instance.name
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)

    def search_test(self, cls, test_against):
        try:
            if self.id != None:
                logging.getLogger("tests").debug(
                        "%s.test_search: id = %d, name = %s",
                        type(self).__name__,
                        self.id,
                        self.name
                    )
                search = test_3times_then_fail(
                        cls.search,
                        self.name,
                        field_list=['id'],
                        timeout=TIMEOUT
                    )
                self.assertNotEqual(len(search),0)
                for c in test_3times_then_fail(list,search):
                    self.assertIsInstance(c, (test_against, type(None)))
                self.assertIn(
                        self.id,
                        [c.id for c in test_3times_then_fail(list,search)]
                    )
            else:
                logging.getLogger("tests").debug(
                        "%s.test_search: id = None => no test",
                        type(self).__name__
                    )
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)

    def get_sample(self,cls):
        try:
            if self.id != None:
                logging.getLogger("tests").debug(
                        "%s.test_get_all_attributes: id = %d, name = %s",
                        type(self).__name__,
                        self.id,
                        self.name
                    )
                return test_3times_then_fail(
                        cls,
                        self.id,
                        all=True,
                        timeout=TIMEOUT
                    )
            else:
                logging.getLogger("tests").debug(
                        "%s.test_get_all_attributes: id = None => no test",
                        type(self).__name__
                    )
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)
