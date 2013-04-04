import pycomicvine
import datetime
from tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestCharactersList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Characters,
                pycomicvine.Character
            )

class TestCharacterAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Characters)

    def test_search(self):
        self.search_test(pycomicvine.Characters, pycomicvine.Character)

    def test_get_all_attributes(self):
        character = self.get_sample(pycomicvine.Character)
        self.assertIsInstance(
                character.api_detail_url, 
                (type(None),basestring)
            )
        self.assertIsInstance(
                character.birth, 
                (type(None), datetime.datetime)
            )
        self.assertIsInstance(
                character.character_enemies,
                pycomicvine.Characters
            )
        self.assertIsInstance(
                character.character_friends,
                pycomicvine.Characters
            )
        self.assertIsInstance(
                character.count_of_issue_appearances,
                int
            )
        self.assertIsInstance(
                character.creators,
                pycomicvine.People
            )
        self.assertIsInstance(
                character.date_added,
                datetime.datetime
            )
        self.assertIsInstance(
                character.date_last_updated,
                datetime.datetime
            )
        self.assertIsInstance(
                character.deck,
                (type(None),basestring)
            )
        self.assertIsInstance(
                character.description,
                (type(None),basestring)
            )
        self.assertIsInstance(
                character.first_appeared_in_issue,
                (type(None),pycomicvine.Issue)
            )
        self.assertIsInstance(
                character.gender,
                unicode
            )
        self.assertIn(
                character.gender,
                [u'\u2842', u'\u2640', u'\u26a7']
            )
        self.assertIsInstance(
                character.id,
                int 
            )
        self.assertIsInstance(
                character.image,
                (type(None),dict)
            )
        self.assertIsInstance(
                character.issue_credits,
                pycomicvine.Issues
            )
        self.assertIsInstance(
                character.issues_died_in,
                pycomicvine.Issues
            )
        self.assertIsInstance(
                character.movies,
                pycomicvine.Movies
            )
        self.assertIsInstance(
                character.name,
                (type(None),basestring)
            )
        self.assertIsInstance(
                character.origin,
                (type(None),pycomicvine.Origin)
            )
        self.assertIsInstance(
                character.powers,
                pycomicvine.Powers
            )
        self.assertIsInstance(
                character.publisher,
                pycomicvine.Publisher
            )
        self.assertIsInstance(
                character.real_name,
                (type(None),basestring)
           )
        self.assertIsInstance(
                character.site_detail_url,
                (type(None),basestring)
            )
        self.assertIsInstance(
                character.story_arc_credits,
                pycomicvine.StoryArcs
            )
        self.assertIsInstance(
                character.team_enemies,
                pycomicvine.Teams
            )
        self.assertIsInstance(
                character.team_friends,
                pycomicvine.Teams
            )
        self.assertIsInstance(
                character.teams,
                pycomicvine.Teams
            )
        self.assertIsInstance(
                character.volume_credits,
                pycomicvine.Volumes
            )
