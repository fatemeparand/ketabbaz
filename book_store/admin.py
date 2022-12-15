from django.contrib import admin
from .models import Book, Subject, Comment

admin.site.register(Subject)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'author', 'status', 'datetime_modified', 'active')
    ordering = ('-datetime_modified',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'author', 'score', 'datetime_created', 'active']
    ordering = ('-datetime_created',)

