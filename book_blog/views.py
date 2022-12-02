from django.shortcuts import render
from .models import BookBlog
from django.shortcuts import get_object_or_404


def book_list_view(request):
    books = BookBlog.objects.filter(status='pub')
    context = {'books': books}
    return render(request, 'book_blog/bookblog_list.html', context)


def book_detail_view(request, book_id):
    book = get_object_or_404(BookBlog, id=book_id)

    context = {'book': book}
    return render(request, 'book_blog/bookblog_detail.html', context)
