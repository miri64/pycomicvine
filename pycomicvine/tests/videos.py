import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestChatsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Chats,
                pycomicvine.Chat
            )

class TestChatAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Chats)

    def test_search(self):
        self.search_test(pycomicvine.Chats, pycomicvine.Chat)

    def test_get_all_attributes(self):
        video = self.get_sample(pycomicvine.Chat)
        if video != None:
            self.assertIsInstance(
                    video.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.deck, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.hd_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.high_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.image, 
                    dict
                )
            self.assertIsInstance(
                    video.length_seconds, 
                    (type(None),int)
                )
            self.assertIsInstance(
                    video.low_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.name, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.publish_date, 
                    (type(None),datetime.datetime)
                )
            self.assertIsInstance(
                    video.site_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    video.user, 
                    (type(None),basestring)
                )
