from django.test import TestCase
from rest_framework import exceptions

from users.models import User
from users.services import UserService


class UserServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = UserService()

    def test_create_user(self):
        payload = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test da Silva",
            "password": "@Test123",
        }

        user = self.service.create_user(payload)

        self.assertIsInstance(user, User)
        self.assertEqual(User.objects.count(), 1)
        self.assertTrue(User.objects.filter(email=payload.get("email")).exists())

    def test_create_user_exception_already_user(self):
        User.objects.create(username='teste123', email='test@gmail.com')

        payload = {
            "username": "teste123",
            "email": "test@gmail.com",
            "full_name": "Test da Silva",
            "password": "@Test123",
        }

        with self.assertRaises(exceptions.APIException) as ctx:
            self.service.create_user(payload)

        self.assertEqual(ctx.exception.detail.title(), 'Já Existe Um Usuário Com Esse Username/Email.')