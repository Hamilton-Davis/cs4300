from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Movie

class MovieAPITestCase(APITestCase):
    def setUp(self):
        self.movie1 = Movie.objects.create(
            title="Sw White",
            description="1",
            release_date="2020-03-20",
            duration=60
        )
        self.movie2 = Movie.objects.create(
            title="Snohite",
            description="2",
            release_date="2025-03-20",
            duration=120
        )
        self.movie3 = Movie.objects.create(
            title="Snow Whe",
            description="3",
            release_date="2019-03-20",
            duration=180
        )

        self.movie_list_url = '/movies/'

    def test_get_movie_list(self):
        response = self.client.get(self.movie_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_post_valid_movie(self):
        data = {
            "title": "Cinderella",
            "description": "Fairy tale",
            "release_date": "2025-12-25",
            "duration": 100
        }
        response = self.client.post(self.movie_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 4)

    def test_post_invalid_movie(self):
        data = {
            "title": "",
            "description": "",
            "release_date": None,
            "duration": None
        }
        response = self.client.post(self.movie_list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
