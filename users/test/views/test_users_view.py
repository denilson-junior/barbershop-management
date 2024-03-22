from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class UserAPIViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.url = reverse("users")

    
    def test_create_user(self):
        payload = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test da Silva",
            "password": "@Test123"
        }

        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, payload)


    def test_create_user_invalid_payload(self):
        payload = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test da Silva"
        }

        response = self.client.post(self.url, payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data["password"][0].title(), "This Field Is Required.")