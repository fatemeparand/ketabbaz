from django.test import TestCase
from django.shortcuts import reverse
from .models import BookBlog
from accounts.models import CustomUser


class BookBlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = CustomUser.objects.create(username='user1')

        cls.bookblog1 = BookBlog.objects.create(
            book_name='book1',
            book_author='author1',
            introduction='introduction1',
            author=cls.user,
            status=BookBlog.STATUS_CHOICES[0][0],  # pub
            book_page=100
        )

        cls.bookblog2 = BookBlog.objects.create(
            book_name='book2',
            book_author='author2',
            introduction='introduction2',
            author=cls.user,
            status=BookBlog.STATUS_CHOICES[1][0],  # drf
            book_page=100
        )

    def test_bookblog_list_url(self):
        response = self.client.get('/book_blog/')
        self.assertEqual(response.status_code, 200)

    def test_bookblog_list_url_by_name(self):
        response = self.client.get(reverse('book_blog:bookblog_list'))
        self.assertEqual(response.status_code, 200)

    def test_book_name_on_bookblog_list_page(self):
        response = self.client.get(reverse('book_blog:bookblog_list'))
        self.assertContains(response, self.bookblog1.book_name)

    def test_bookblog_detail_url(self):
        response = self.client.get(f'/book_blog/{self.bookblog1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_bookblog_detail_url_by_name(self):
        response = self.client.get(reverse('book_blog:bookblog_detail', args=[self.bookblog1.id]))
        self.assertEqual(response.status_code, 200)

    def test_bookblog_detail_on_bookblog_detail_page(self):
        response = self.client.get(reverse('book_blog:bookblog_detail', args=[self.bookblog1.id]))
        self.assertContains(response, self.bookblog1.book_name)
        self.assertContains(response, self.bookblog1.introduction)

    def test_status_404_if_bookblog_id_not_exist(self):
        response = self.client.get(reverse('book_blog:bookblog_detail', args=[9999]))
        self.assertEqual(response.status_code, 404)

    def test_drf_bookblogs_not_show_in_bookblog_list(self):
        response = self.client.get(reverse('book_blog:bookblog_list'))
        self.assertContains(response, self.bookblog1.book_name)
        self.assertNotContains(response, self.bookblog2.book_name)

    def test_book_model_str(self):
        self.assertEqual(str(self.bookblog1), self.bookblog1.book_name)

    def test_book_detail(self):
        self.assertEqual(self.bookblog1.book_name, 'book1')
        self.assertEqual(self.bookblog1.book_author, 'author1')
        self.assertEqual(self.bookblog1.introduction, 'introduction1')
        self.assertEqual(self.bookblog1.author, self.user)

    # create book
    def test_book_create_view(self):
        response = self.client.post(reverse('book_blog:bookblog_create'), {
            'book_name': 'book1',
            'book_author': 'author1',
            'introduction': 'introduction1',
            'author': self.user.id,
            'status': BookBlog.STATUS_CHOICES[0][0],  # pub
            'book_page': 100,
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual(BookBlog.objects.last().book_name, 'book1')
        self.assertEqual(BookBlog.objects.last().book_author, 'author1')
        self.assertEqual(BookBlog.objects.last().introduction, 'introduction1')

    # update book
    def test_book_update_view(self):
        response = self.client.post(reverse('book_blog:bookblog_update', args=[self.bookblog2.id]), {
            'book_name': 'book2 updated',
            'book_author': 'author2',
            'introduction': 'introduction2 updated',
            'author': self.bookblog2.author.id,
            'status': 'drf',
            'book_page': 100,
        })

        self.assertEqual(response.status_code, 302)

        self.assertEqual(BookBlog.objects.last().book_name, 'book2 updated')
        self.assertEqual(BookBlog.objects.last().introduction, 'introduction2 updated')

    # delete book
    def test_book_delete_view(self):
        response = self.client.post(reverse('book_blog:bookblog_delete', args=[self.bookblog1.id]))

        self.assertEqual(response.status_code, 302)
