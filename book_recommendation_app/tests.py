from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookManagementTestCase(APITestCase):
    def test_add_book(self):
        data = {
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "genre": "Fiction",
            "published_date": "1925-04-10"
        }
        response = self.client.post("/api/books/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "The Great Gatsby")

    def test_list_books(self):
        Book.objects.create(title="1984", author="George Orwell", genre="Dystopian", published_date="1949-06-08")
        Book.objects.create(title="To Kill a Mockingbird", author="Harper Lee", genre="Fiction", published_date="1960-07-11")
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
