from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class BookBlog(models.Model):
    STATUS_CHOICES = (
        ('pub', 'published'),
        ('drf', 'draft'),
    )

    book_name = models.CharField(max_length=100, verbose_name=_('book name'))
    book_author = models.CharField(max_length=100, verbose_name=_('book author'))
    # release_date = models.PositiveIntegerField(max_length=4, verbose_name=_('release date'))
    introduction = models.TextField(verbose_name=_('introduction'))
    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('time created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('time modified'))
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('author'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=3, verbose_name=_('status'))
    book_page = models.PositiveIntegerField(verbose_name=_('number of book page'))

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book_blog:bookblog_detail', args=[self.id])
