import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestIssuesList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Issues,
                pycomicvine.Issue
            )

class TestIssueAttributes(SingularResourceTestCase):
    def setUp(self):
        self.name = None
        while self.name == None:
            self.get_random_instance(pycomicvine.Issues)
            try:
                if self.name == None:
                    issue = test_3times_then_fail(
                            pycomicvine.Issue,
                            self.id,
                            field_lis=['volume','issue_number'],
                            timeout=TIMEOUT
                        )
                    self.name = issue.volume.name+" "+\
                            str(issue.issue_number)
            except TimeoutError,e:
                logging.getLogger("tests").debug(e)


    def test_search(self):
        self.search_test(pycomicvine.Issues, pycomicvine.Issue)

    def test_get_all_attributes(self):
        issue = self.get_sample(pycomicvine.Issue)
        if issue != None:
            self.assertIsInstance(
                    issue.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    issue.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    issue.character_credits,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    issue.cover_date, 
                    (type(None), datetime.datetime)
                )
            self.assertIsInstance(
                    issue.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    issue.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    issue.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    issue.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    issue.disbanded_teams,
                    pycomicvine.Teams
                )
            self.assertIsInstance(
                    issue.first_appearance_characters,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    issue.first_appearance_concepts,
                    pycomicvine.Concepts
                )
            self.assertIsInstance(
                    issue.first_appearance_locations,
                    pycomicvine.Locations
                )
            self.assertIsInstance(
                    issue.first_appearance_objects,
                    pycomicvine.Objects
                )
            self.assertIsInstance(
                    issue.first_appearance_storyarcs,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    issue.first_appearance_teams,
                    pycomicvine.Teams
                )
            self.assertIsInstance(
                    issue.has_staff_review,
                    bool
                )
            self.assertIsInstance(
                    issue.id,
                    int 
                )
            self.assertIsInstance(
                    issue.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    issue.issue_number,
                    (type(None),int)
                )
            self.assertIsInstance(
                    issue.location_credits,
                    pycomicvine.Locations
                )
            self.assertIsInstance(
                    issue.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    issue.object_credits,
                    pycomicvine.Objects
                )
            self.assertIsInstance(
                    issue.person_credits,
                    pycomicvine.People
                )
            self.assertIsInstance(
                    issue.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    issue.store_date,
                    (type(None),datetime.datetime)
                )
            self.assertIsInstance(
                    issue.story_arc_credits,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    issue.team_credits,
                    pycomicvine.Teams
                )
            self.assertIsInstance(
                    issue.teams_disbanded_in,
                    pycomicvine.Teams
                )
            self.assertIsInstance(
                    issue.volume,
                    (type(None),pycomicvine.Volume)
                )
