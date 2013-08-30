import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestPromosList(ListResourceTestCase):
    def test_get_id_and_name(self):
        try:
            promos = test_3times_then_fail(
                    pycomicvine.Promos,
                    field_list=['name','id'],
                    timeout=TIMEOUT
                )
            assertionFails = 0
            for c in test_3times_then_fail(list,promos):
                if not isinstance(c, pycomicvine.Promo):
                    assertionFails += 1
                else:
                    self.assertIsInstance(c, pycomicvine.Promo)
            # there is one odd empty list in the results of
            # /promos. Just checking if it will stay there
            self.assertLessEqual(assertionFails, 1)
        except TimeoutError,e:
            logging.getLogger("tests").debug(e)

class TestPromoAttributes(SingularResourceTestCase):
    def setUp(self):
        self.id, self.name = None, None
        while self.id == None and self.name == None:
            try:
                self.get_random_instance(pycomicvine.Promos)
            except AttributeError:
                # Jump over the strange empty slot if nessasary
                continue

    def test_get_all_attributes(self):
        promo = self.get_sample(pycomicvine.Promo)
        if promo != None:
            self.assertIsInstance(
                    promo.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    promo.date_added, 
                    (type(None),datetime.datetime)
                )
            self.assertIsInstance(
                    promo.deck, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    promo.id, 
                    int
                )
            self.assertIsInstance(
                    promo.image, 
                    dict
                )
            self.assertIsInstance(
                    promo.link, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    promo.name, 
                    (type(None),basestring)
                )
