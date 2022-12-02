from django.shortcuts import render
from .models import BookBlog


def book_list_view(request):
    books = BookBlog.objects.all()
    context = {'books': books}
    return render(request, 'book_blog/bookblog_list.html', context)
