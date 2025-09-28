from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user (for authentication if needed)
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()
        self.client.login(username="testuser", password="password123")

        # Create some test books
        self.book1 = Book.objects.create(title="Python Basics", author="John Doe", publication_year=2020)
        self.book2 = Book.objects.create(title="Advanced Django", author="Jane Smith", publication_year=2022)

        self.book_list_url = reverse('book-list')  # assumes you named it in urls.py

    def test_create_book(self):
        data = {"title": "New Book", "author": "Alice", "publication_year": 2021}
        response = self.client.post(self.book_list_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.get(id=response.data["id"]).title, "New Book")

    def test_get_books_list(self):
        response = self.client.get(self.book_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # 2 books created in setUp

    def test_update_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {"title": "Updated Python", "author": "John Doe", "publication_year": 2020}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Python")

    def test_delete_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_year(self):
        response = self.client.get(self.book_list_url, {"publication_year": 2022})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Advanced Django")

    def test_search_books(self):
        response = self.client.get(self.book_list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "John Doe")

    def test_order_books_by_year(self):
        response = self.client.get(self.book_list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Advanced Django")  # newest first
