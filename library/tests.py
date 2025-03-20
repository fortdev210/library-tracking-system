from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token

from .models import Book, Member, Loan, Author


# Create your tests here.

class BookViewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="jeff", password="password")
        self.token, _ = Token.objects.get_or_create(user=self.user) 
        self.author = Author.objects.create(first_name="john", last_name="doe", biography="a wonderful novelist")
        self.book = Book.objects.create(title='Test Book', author_id=self.author.id, genre="sci-fi", available_copies=5, isbn="978")
        self.client.credentials(HTTP_AUTHORIZATION='Token '+self.token.key)
        self.member = Member.objects.create(user=self.user)
        
        
    def test_loan_book_view(self):
        response = self.client.post('/api/books/{}/loan/'.format(self.book.id), {'member_id': self.member.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        loan = Loan.objects.get(book=self.book, member=self.member)
        self.assertIsNotNone(loan.id)
        self.assertEqual(loan.is_returned, False)