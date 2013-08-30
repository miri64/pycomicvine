import pycomicvine
import unittest
from tests.utils import test_3times_then_fail, TimeoutError

api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestSearch(unittest.TestCase):
    def test_search_resource_type(self):
        try:
            search = test_3times_then_fail(
                    pycomicvine.Search,
                    resources="volume", 
                    query="Angel"
                )
            for v in test_3times_then_fail(list, search):
                self.assertIsInstance(v, pycomicvine.Volume)
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)

    def test_search_id(self):
        try:
            search = test_3times_then_fail(
                    pycomicvine.Search,
                    query="The Walking Dead",
                    field_list=["id"]
                )
            self.assertNotEqual(len(search),0)
            self.assertIn(18166, [s.id for s in search])
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)
