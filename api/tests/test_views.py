from rest_framework.test import APITestCase
from api.models import Movie
from django.urls import reverse


class TestMovieApi(APITestCase):

    def setUp(self):
        self.movie = Movie(name='Infinity War', year_of_release=2018)
        self.movie.save()

    def test_movie_creation(self):
        resp = self.client.post(reverse('movies'), {
            'name': 'The Incredibles 2',
            'year_of_release': 2018
        })

        self.assertEquals(Movie.objects.count(), 2)
        self.assertEquals(201, resp.status_code)

    def test_get_movies(self):
        resp = self.client.get(reverse('movies'), format='json')
        self.assertEquals(len(resp.data), 1)

    def test_update_movie(self):
        resp = self.client.put(reverse('detail', kwargs={'pk': 1}), {
            'name': 'The Incredibles 2 UPDATED',
            'year_of_release': 2018
        }, format='json')

        self.assertEquals('The Incredibles 2 UPDATED', resp.data['name'])

    def test_delete_movie(self):
        resp = self.client.delete(reverse('detail', kwargs={'pk': 1}))

        self.assertEquals(204, resp.status_code)


