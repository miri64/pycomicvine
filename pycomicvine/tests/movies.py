import pycomicvine
import datetime
from pycomicvine.tests.utils import *

pycomicvine.api_key = "476302e62d7e8f8f140182e36aebff2fe935514b"

class TestMoviesList(ListResourceTestCase):
    def test_get_id_and_name(self):
        self.get_id_and_name_test(
                pycomicvine.Movies,
                pycomicvine.Movie
            )

class TestMovieAttributes(SingularResourceTestCase):
    def setUp(self):
        self.get_random_instance(pycomicvine.Movies)

    def test_search(self):
        self.search_test(pycomicvine.Movies, pycomicvine.Movie)

    def test_get_all_attributes(self):
        movie = self.get_sample(pycomicvine.Movie)
        if movie != None:
            self.assertIsInstance(
                    movie.api_detail_url, 
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.box_office_revenue, 
                    (type(None), int)
                )
            self.assertIsInstance(
                    movie.budget, 
                    (type(None), int)
                )
            self.assertIsInstance(
                    movie.characters,
                    pycomicvine.Characters
                )
            self.assertIsInstance(
                    movie.concepts,
                    pycomicvine.Concepts
                )
            self.assertIsInstance(
                    movie.date_added,
                    datetime.datetime
                )
            self.assertIsInstance(
                    movie.date_last_updated,
                    datetime.datetime
                )
            self.assertIsInstance(
                    movie.deck,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.description,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.distributor,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.has_staff_review,
                    (type(None),bool)
                )
            self.assertIsInstance(
                    movie.id,
                    int 
                )
            self.assertIsInstance(
                    movie.image,
                    (type(None),dict)
                )
            self.assertIsInstance(
                    movie.locations,
                    pycomicvine.Locations
                )
            self.assertIsInstance(
                    movie.name,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.producers,
                    pycomicvine.People
                )
            self.assertIsInstance(
                    movie.rating,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.release_date,
                    (type(None),datetime.datetime)
                )
            self.assertIsInstance(
                    movie.runtime,
                    (type(None),int)
               )
            self.assertIsInstance(
                    movie.site_detail_url,
                    (type(None),basestring)
                )
            self.assertIsInstance(
                    movie.studios,
                    (type(None),list)
                )
            self.assertIsInstance(
                    movie.teams,
                    pycomicvine.Teams
                )
            self.assertIsInstance(
                    movie.things,
                    pycomicvine.Objects
                )
            self.assertIsInstance(
                    movie.total_revenue,
                    (type(None),int)
                )
            self.assertIsInstance(
                    movie.writers,
                    pycomicvine.People
                )
