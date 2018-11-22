from django.test import TestCase
from api.models import Movie


# Create your tests here.
class TestMovieModel(TestCase):

    def setUp(self):
        self.movie = Movie(name='DeadPool 2', year_of_release=2018)
        self.movie.save()

    def test_movie_created(self):
        self.assertEquals(Movie.objects.count(), 1)

    def test_movie_str(self):
        self.assertEquals(self.movie.name, str(self.movie))
