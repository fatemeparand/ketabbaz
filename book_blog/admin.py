from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'author', 'status', 'datetime_modified')
    ordering = ('-datetime_modified',)
