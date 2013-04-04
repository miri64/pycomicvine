import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestVideoTypesList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.VideoTypes,
                pycomicvine.VideoType
            )

class TestVideoTypeAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.VideoTypes)

    def test_get_all_attributes(self):
        video_type = self.get_sample(pycomicvine.VideoType)
        if video_type != None:
            self.assertIsInstance(
                    video_type.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video_type.deck, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video_type.id, 
                    int
                )
            self.assertIsInstance(
                    video_type.name, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video_type.site_detail_url, 
                    (type(None),basestring)
                )
