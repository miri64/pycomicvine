import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestObjectsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Objects,
                pycomicvine.Object
            )

class TestObjectAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Objects)

    def test_search(self):
        self.search_test(pycomicvine.Objects, pycomicvine.Object)

    def test_get_all_attributes(self):
        object = self.get_sample(pycomicvine.Object)
        if object != None:
            self.assertIsInstance(
                    object.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    object.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    object.count_of_issue_appearances,
                    int
                )
            self.assertIsInstance(
                    object.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    object.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    object.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    object.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    object.first_appeared_in_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    object.id,
                    int 
                )
            self.assertIsInstance(
                    object.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    object.issue_credits,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    object.movies,
                    pycomicvine.Movies
                )
            self.assertIsInstance(
                    object.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    object.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    object.start_year,
                    (type(None),int)
                )
            self.assertIsInstance(
                    object.story_arc_credits,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    object.volume_credits,
                    pycomicvine.Volumes
                )
