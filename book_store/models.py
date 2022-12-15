from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class Subject(models.Model):
    subject = models.CharField(max_length=200, verbose_name=_('subject'))

    def __str__(self):
        return self.subject


class Book(models.Model):
    STATUS_CHOICES = (
        ('preparing', _('Preparing')),
        ('available', _('Available')),
        ('not available', _('Not Available')),
    )

    book_name = models.CharField(max_length=100, verbose_name=_('book name'))
    book_author = models.CharField(max_length=100, verbose_name=_('book author'))
    translator = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('translator'))
    publisher = models.CharField(max_length=50, verbose_name=_('publisher'))
    publication_year = models.PositiveIntegerField(verbose_name=_('publication year'))

    description = models.TextField(verbose_name=_('book description'))
    price = models.PositiveIntegerField(default=0, verbose_name=_('price'))
    book_page = models.PositiveIntegerField(verbose_name=_('number of book page'), blank=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name=_('author'))
    status = models.CharField(choices=STATUS_CHOICES, max_length=13, verbose_name=_('status'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name=_('subject'),)
    image = models.ImageField(upload_to='book_cover/', blank=True, verbose_name=_('book image'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('time created'))
    datetime_modified = models.DateTimeField(auto_now=True, verbose_name=_('time modified'))

    def __str__(self):
        return self.book_name

    def get_absolute_url(self):
        return reverse('book_store:book_detail', args=[self.id])


class Comment(models.Model):
    BOOK_SCORE = (
        ('1', _('Very Bad')),
        ('2', _('Bad')),
        ('3', _('Normal')),
        ('4', _('Good')),
        ('5', _('Perfect')),
    )

    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('comment body'),
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name=_('comment author'),
    )
    body = models.TextField(verbose_name=_('comment body'))
    score = models.CharField(choices=BOOK_SCORE, max_length=10, verbose_name=_('Your Score'))

    datetime_created = models.DateTimeField(auto_now_add=True, verbose_name=_('time create'))
    active = models.BooleanField(default=True, verbose_name=_('active status'))
    recommend = models.BooleanField(default=True, verbose_name=_('i recommend this book'))

    def __str__(self):
        return self.body

    def get_absolute_url(self):
        return reverse('book_store:book_detail', args=[self.book.id])
