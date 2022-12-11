from django.contrib import admin
from .models import Book
from .models import Subject

admin.site.register(Subject)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'author', 'status', 'datetime_modified', 'active')
    ordering = ('-datetime_modified',)


