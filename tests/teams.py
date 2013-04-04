import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestTeamsList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Teams,
                pycomicvine.Team
            )

class TestTeamAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Teams)

    def test_search(self):
        self.search_test(pycomicvine.Teams, pycomicvine.Team)

    def test_get_all_attributes(self):
        team = self.get_sample(pycomicvine.Team)
        if team != None:
            self.assertIsInstance(
                    team.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    team.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    team.character_enemies,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    team.character_friends,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    team.characters,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    team.count_of_issue_appearances,
                    int
                )
            self.assertIsInstance(
                    team.count_of_team_members,
                    (type(None),int)
                )
            self.assertIsInstance(
                    team.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    team.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    team.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    team.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    team.first_appeared_in_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    team.id,
                    int 
                )
            self.assertIsInstance(
                    team.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    team.issue_credits,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    team.issues_disbanded_in,
                    pycomicvine.Issues
                )
            self.assertIsInstance(
                    team.movies,
                    pycomicvine.Movies
                )
            self.assertIsInstance(
                    team.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    team.publisher,
                    (type(None),pycomicvine.Publisher)
                )
            self.assertIsInstance(
                    team.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    team.story_arc_credits,
                    pycomicvine.StoryArcs
                )
            self.assertIsInstance(
                    team.volume_credits,
                    pycomicvine.Volumes
                )
