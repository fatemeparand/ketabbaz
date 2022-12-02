from django.contrib import admin
from .models import BookBlog


@admin.register(BookBlog)
class BookBlogAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'author', 'status')
