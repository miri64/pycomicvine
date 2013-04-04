import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestLocationsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Locations,
                pycomicvine.Location
            )

class TestLocationAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Locations)

    def test_search(self):
        self.search_test(pycomicvine.Locations, pycomicvine.Location)

    def test_get_all_attributes(self):
        location = self.get_sample(pycomicvine.Location)
        if location != None:
            self.assertIsInstance(
                    location.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    location.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    location.count_of_issue_appearances,
                    int
                )
            self.assertIsInstance(
                    location.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    location.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    location.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    location.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    location.first_appeared_in_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    location.id,
                    int 
                )
            self.assertIsInstance(
                    location.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    location.issue_credits,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    location.movies,
                    pycomicvine.Movies
                )
            self.assertIsInstance(
                    location.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    location.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    location.start_year,
                    (type(None),int)
                )
            self.assertIsInstance(
                    location.story_arc_credits,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    location.volume_credits,
                    pycomicvine.Volumes
                )
