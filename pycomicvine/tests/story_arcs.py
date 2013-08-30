import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestStoryArcsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.StoryArcs,
                pycomicvine.StoryArc
            )

class TestStoryArcAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.StoryArcs)

    def test_search(self):
        self.search_test(pycomicvine.StoryArcs, pycomicvine.StoryArc)

    def test_get_all_attributes(self):
        story_arc = self.get_sample(pycomicvine.StoryArc)
        if story_arc != None:
            self.assertIsInstance(
                    story_arc.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    story_arc.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    story_arc.count_of_issue_appearances,
                    int
                )
            self.assertIsInstance(
                    story_arc.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    story_arc.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    story_arc.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    story_arc.first_appeared_in_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    story_arc.id,
                    int 
                )
            self.assertIsInstance(
                    story_arc.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    story_arc.issues,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    story_arc.movies,
                    pycomicvine.Movies
                )
            self.assertIsInstance(
                    story_arc.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    story_arc.publisher,
                    (type(None),pycomicvine.Publisher)
                )
            self.assertIsInstance(
                    story_arc.site_detail_url,
                    (type(None),basestring)
                )
