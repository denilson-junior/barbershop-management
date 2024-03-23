from django.test import TestCase
from users.serializers import UserCreateSerializer


class UserCreateSerializerTestCase(TestCase):
    def test_user_serializer_valid(self):
        data = {
            "username": "test",
            "email": "test@test.com",
            "full_name": "Test 123",
            "password": "@Test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertTrue(serializer.is_valid())

    def test_user_serializer_invalid(self):
        data = {"full_name": "Test 123", "password": "@test123"}

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())

    def test_user_serializer_username_invalid(self):
        data = {
            "username": "t",
            "email": "test@test.com",
            "full_name": "Test 123",
            "password": "@test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())

    def test_user_serializer_email_invalid(self):
        data = {
            "username": "test",
            "email": "#test@test.com",
            "full_name": "Test 123",
            "password": "@test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())

    def test_user_serializer_password_invalid(self):
        data = {
            "username": "test",
            "email": "#test@test.com",
            "full_name": "Test 123",
            "password": "Test123",
        }

        serializer = UserCreateSerializer(data=data)

        self.assertFalse(serializer.is_valid())
        self.assertEqual(
            serializer.errors["password"][0].title(),
            "A Senha Deve Ter Pelo Menos Um Caracter Especial.",
        )
