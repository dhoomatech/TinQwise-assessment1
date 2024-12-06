from rest_framework.test import APITestCase
from rest_framework import status
from user_app.models import User,UserPreference
from book_recommendation_app.models import Book

class UserManagementTestCase(APITestCase):
    def test_add_user(self):
        data = {"username": "vishnu", "email": "vishnu@example.com", "password": "vishnu123"}
        response = self.client.post("/api/users/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "vishnu")

    def test_retrieve_user(self):
        user = User.objects.create_user(username="vishnu", email="vishnu@example.com", password="vishnu123")
        response = self.client.get(f"/api/users/{user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "vishnu")


class UserPreferenceTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="password123")
        self.book = Book.objects.create(title="1984", author="George Orwell", genre="Dystopian", published_date="1949-06-08")

    def test_add_user_preference(self):
        data = {"book": self.book.id, "preference": "like"}
        url = f"/api/users/{self.user.id}/preferences/"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_prevent_duplicate_preference(self):
        UserPreference.objects.create(user=self.user, book=self.book, preference="like")
        data = {"book": self.book.id, "preference": "like"}
        response = self.client.post(f"/api/users/{self.user.id}/preferences/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reset_preferences(self):
        UserPreference.objects.create(user=self.user, book=self.book, preference="like")
        url = f"/api/users/{self.user.id}/preferences/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UserPreference.objects.filter(user=self.user).count(), 0)
    
    def test_user_recommendations(self):
        url = f"/api/users/{self.user.id}/recommendations/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    


