import pycomicvine
import unittest
import random
import datetime
import logging
from tests.utils import test_3times_then_fail

TIMEOUT=10

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestCharactersList(unittest.TestCase):
    def test_get_id_and_name(self):
        characters = test_3times_then_fail(
                pycomicvine.Characters,
                field_list=['name','id'],
                limit=1,
                timeout=TIMEOUT
            )
        rand_offset = random.randint(1,len(characters)-100)
        max_index = random.randint(
                rand_offset,
                min(len(characters), rand_offset+300)
            )
        characters = test_3times_then_fail(
                pycomicvine.Characters,
                field_list=['name','id'],
                limit=100,
                offset=rand_offset,
                timeout=TIMEOUT
            )
        self.assertNotEqual(len(characters), 0)
        for c in test_3times_then_fail(list,characters[
                rand_offset:max_index
            ]):
            self.assertIsInstance(c, pycomicvine.Character)

class TestCharacterAttributes(unittest.TestCase):
    def setUp(self):
        characters = test_3times_then_fail(
                pycomicvine.Characters,
                field_list=['id','name'],
                timeout=TIMEOUT
            )
        rand_character = random.choice(characters)
        self.id, self.name = rand_character.id, rand_character.name 

    def test_search(self):
        logging.getLogger("tests").debug(
                "%s.test_search: id = %d, name = %s",
                type(self).__name__,
                self.id,
                self.name
            )
        search = test_3times_then_fail(
                pycomicvine.Characters.search,
                self.name,
                field_list=['id'],
                timeout=TIMEOUT
            )
        self.assertNotEqual(len(search),0)
        for c in test_3times_then_fail(list,search):
            self.assertIsInstance(c, pycomicvine.Character)
        self.assertIn(
                self.id, 
                [c.id for c in test_3times_then_fail(list,search)]
            )

    def test_get_all_attributes(self):
        logging.getLogger("tests").debug(
                "%s.test_get_all_attributes: id = %d, name = %s",
                type(self).__name__,
                self.id,
                self.name
            )
        character = test_3times_then_fail(
                pycomicvine.Character,
                self.id, 
                all=True,
                timeout=TIMEOUT
            )

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
