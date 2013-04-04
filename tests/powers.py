import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestPowersList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Powers,
                pycomicvine.Power
            )

class TestPowerAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Powers)

    def test_get_all_attributes(self):
        power = self.get_sample(pycomicvine.Power)
        if power != None:
            self.assertIsInstance(
                    power.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    power.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    power.characters,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    power.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    power.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    power.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    power.id,
                    int 
                )
            self.assertIsInstance(
                    power.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    power.site_detail_url,
                    (type(None),basestring)
                )
