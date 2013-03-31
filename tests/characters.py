import pycomicvine
import unittest
import random
import datetime
import logging

MAX_TESTS = 3

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestCharactersList(unittest.TestCase):
    def test_get_id_and_name(self):
        characters = pycomicvine.Characters(field_list=['name','id'])
        self.assertNotEqual(len(characters), 0)
        for c in characters:
            self.assertIsInstance(c, pycomicvine.Character)

class TestCharacterAttributes(unittest.TestCase):
    def setUp(self):
        characters = pycomicvine.Characters(field_list=['id','name'])
        self.id, self.name = random.choice(
                [(c.id, c.name) for c in characters[:100]]
            )

    def test_search(self):
        logging.getLogger("tests").debug(
                "%s.test_search: id = %d, name = %s",
                type(self).__name__,
                self.id,
                self.name
            )
        search = pycomicvine.Character.search(
                self.name,
                field_list=['id']
            )
        self.assertNotEqual(len(search),0)
        for c in search:
            self.assertIsInstance(c, pycomicvine.Character)
        self.assertIn(self.id, [c.id for c in search])

    def test_get_all_attributes(self):
        logging.getLogger("tests").debug(
                "%s.test_get_all_attributes: id = %d, name = %s",
                type(self).__name__,
                self.id,
                self.name
            )
        character = pycomicvine.Character(self.id, all=True)

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
                pycomicvine.Issue
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
                pycomicvine.Origin
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
