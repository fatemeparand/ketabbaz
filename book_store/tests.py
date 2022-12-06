from django.test import TestCase
from django.shortcuts import reverse
from .models import Book
from accounts.models import CustomUser


class BookStoreTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(username='user1')

        cls.book1 = Book.objects.create(
            book_name='book1',
            book_author='author1',
            description='description1',
            author=cls.user,
            status=Book.STATUS_CHOICES[0][0],  # pub
            book_page=100
        )

        cls.book2 = Book.objects.create(
            book_name='book2',
            book_author='author2',
            description='description2',
            author=cls.user,
            status=Book.STATUS_CHOICES[1][0],  # drf
            book_page=100
        )

    def test_book_list_url(self):
        response = self.client.get('/book/')
        self.assertEqual(response.status_code, 200)

    def test_book_list_url_by_name(self):
        response = self.client.get(reverse('book_store:book_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_name_on_book_list_page(self):
        response = self.client.get(reverse('book_store:book_list'))
        self.assertContains(response, self.book1.book_name)

    def test_book_detail_url(self):
        response = self.client.get(f'/book/{self.book1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_book_detail_url_by_name(self):
        response = self.client.get(reverse('book_store:book_detail', args=[self.book1.id]))
        self.assertEqual(response.status_code, 200)

    def test_book_detail_on_book_detail_page(self):
        response = self.client.get(reverse('book_store:book_detail', args=[self.book1.id]))
        self.assertContains(response, self.book1.book_name)
        self.assertContains(response, self.book1.description)

    def test_status_404_if_book_id_not_exist(self):
        response = self.client.get(reverse('book_store:book_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_drf_books_not_show_in_book_list(self):
        response = self.client.get(reverse('book_store:book_list'))
        self.assertContains(response, self.book1.book_name)
        self.assertNotContains(response, self.book2.book_name)

    def test_book_model_str(self):
        self.assertEqual(str(self.book1), self.book1.book_name)

    def test_book_detail(self):
        self.assertEqual(self.book1.book_name, 'book1')
        self.assertEqual(self.book1.book_author, 'author1')
        self.assertEqual(self.book1.description, 'description1')
        self.assertEqual(self.book1.author, self.user)

    # create book
    def test_book_create_view(self):
        response = self.client.post(reverse('book_store:book_create'), {
            'book_name': 'book1',
            'book_author': 'author1',
            'description': 'description1',
            'author': self.user.id,
            'status': Book.STATUS_CHOICES[0][0],  # pub
            'book_page': 100,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.last().book_name, 'book1')
        self.assertEqual(Book.objects.last().book_author, 'author1')
        self.assertEqual(Book.objects.last().description, 'description1')

    # update book
    def test_book_update_view(self):
        response = self.client.post(reverse('book_store:book_update', args=[self.book2.id]), {
            'book_name': 'book2 updated',
            'book_author': 'author2',
            'description': 'description2 updated',
            'author': self.book2.author.id,
            'status': 'drf',
            'book_page': 100,
        })

        self.assertEqual(response.status_code, 302)

        self.assertEqual(Book.objects.last().book_name, 'book2 updated')
        self.assertEqual(Book.objects.last().description, 'description2 updated')

    # delete book
    def test_book_delete_view(self):
        response = self.client.post(reverse('book_store:book_delete', args=[self.book1.id]))

        self.assertEqual(response.status_code, 302)
