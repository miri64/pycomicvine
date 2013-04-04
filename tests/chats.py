import pycomicvine
import datetime
from tests.utils import *

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

    def test_get_all_attributes(self):
        chat = self.get_sample(pycomicvine.Chat)
        if chat != None:
            self.assertIsInstance(
                    chat.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    chat.channel_name, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    chat.deck, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    chat.image, 
                    dict
                )
            self.assertIsInstance(
                    chat.password, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    chat.site_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    chat.title, 
                    (type(None),basestring)
                )
