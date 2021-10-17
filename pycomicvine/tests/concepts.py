import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestConceptsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Concepts,
                pycomicvine.Concept
            )

class TestConceptAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Concepts)

    def test_search(self):
        self.search_test(pycomicvine.Concepts, pycomicvine.Concept)

    def test_get_all_attributes(self):
        concept = self.get_sample(pycomicvine.Concept)
        if concept != None:
            self.assertIsInstance(
                    concept.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    concept.api_detail_url, 
                    (type(None),str)
                )
            self.assertIsInstance(
                    concept.count_of_issue_appearances,
                    int
                )
            self.assertIsInstance(
                    concept.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    concept.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    concept.deck,
                    (type(None),str)
                )
            self.assertIsInstance(
                    concept.description,
                    (type(None),str)
                )
            self.assertIsInstance(
                    concept.first_appeared_in_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    concept.id,
                    int 
                )
            self.assertIsInstance(
                    concept.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    concept.issue_credits,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    concept.movies,
                    pycomicvine.Movies
                )
            self.assertIsInstance(
                    concept.name,
                    (type(None),str)
                )
            self.assertIsInstance(
                    concept.site_detail_url,
                    (type(None),str)
                )
            self.assertIsInstance(
                    concept.start_year,
                    (type(None),int)
                )
            self.assertIsInstance(
                    concept.volume_credits,
                    pycomicvine.Volumes
                )
