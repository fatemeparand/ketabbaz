from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from .models import BookBlog
from .forms import BookForm


def book_list_view(request):
    books = BookBlog.objects.filter(status='pub').order_by('-datetime_modified')
    context = {'books': books}
    return render(request, 'book_blog/bookblog_list.html', context)


def book_detail_view(request, book_id):
    book = get_object_or_404(BookBlog, id=book_id)

    context = {'book': book}
    return render(request, 'book_blog/bookblog_detail.html', context)


def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_blog:bookblog_list')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'book_blog/bookblog_create.html', context)


def book_update_view(request, book_id):
    book = get_object_or_404(BookBlog, id=book_id)
    form = BookForm(instance=book, data=request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('book_blog:bookblog_list')

    context = {'form': form}
    return render(request, 'book_blog/bookblog_create.html', context)


def book_delete_view(request, book_id):
    book = get_object_or_404(BookBlog, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_blog:bookblog_list')

    context = {'book': book}
    return render(request, 'book_blog/bookblog_delete.html', context)

