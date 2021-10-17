import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestVolumesList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Volumes,
                pycomicvine.Volume
            )

class TestVolumeAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Volumes)

    def test_search(self):
        self.search_test(pycomicvine.Volumes, pycomicvine.Volume)

    def test_get_all_attributes(self):
        volume = self.get_sample(pycomicvine.Volume)
        if volume != None:
            self.assertIsInstance(
                    volume.aliases, 
                    (type(None),list)
                )
            self.assertIsInstance(
                    volume.api_detail_url, 
                    (type(None),str)
                )
            self.assertIsInstance(
                    volume.character_credits,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    volume.concept_credits,
                    pycomicvine.Concepts
                )
            self.assertIsInstance(
                    volume.count_of_issues,
                    int
                )
            self.assertIsInstance(
                    volume.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    volume.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    volume.deck,
                    (type(None),str)
                )
            self.assertIsInstance(
                    volume.description,
                    (type(None),str)
                )
            self.assertIsInstance(
                    volume.first_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    volume.id,
                    int 
                )
            self.assertIsInstance(
                    volume.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    volume.last_issue,
                    (type(None),pycomicvine.Issue)
                )
            self.assertIsInstance(
                    volume.location_credits,
                    pycomicvine.Locations
                )
            self.assertIsInstance(
                    volume.name,
                    (type(None),str)
                )
            self.assertIsInstance(
                    volume.object_credits,
                    pycomicvine.Objects
                )
            self.assertIsInstance(
                    volume.person_credits,
                    pycomicvine.People
                )
            self.assertIsInstance(
                    volume.publisher,
                    (type(None),pycomicvine.Publisher)
                )
            self.assertIsInstance(
                    volume.site_detail_url,
                    (type(None),str)
                )
            self.assertIsInstance(
                    volume.start_year,
                    (type(None),int)
                )
            with self.assertRaises(AttributeError):
                volume.team_credits # not in API despite documentation
