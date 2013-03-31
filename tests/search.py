import pycomicvine
import unittest

class TestSearch(unittest.TestCase):
    def setUp(self):
        pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

    def test_search_resource_type(self):
        search = pycomicvine.Search(
                resources="volume", 
                query="Angel"
            )
        self.assertTrue(isinstance(search[0], pycomicvine.Volume))

