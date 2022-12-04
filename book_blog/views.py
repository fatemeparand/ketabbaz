from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from .models import BookBlog
from .forms import BookForm


class BookListView(generic.ListView):
    context_object_name = 'books'
    template_name = 'book_blog/bookblog_list.html'

    def get_queryset(self):
        return BookBlog.objects.filter(status='pub').order_by('-datetime_modified')


class BookDetailView(generic.DetailView):
    model = BookBlog
    context_object_name = 'book'
    template_name = 'book_blog/bookblog_detail.html'


class BookCreateView(generic.CreateView):
    model = BookBlog
    form_class = BookForm
    context_object_name = 'form'
    template_name = 'book_blog/bookblog_create.html'


class BookUpdateView(generic.UpdateView):
    model = BookBlog
    form_class = BookForm
    context_object_name = 'form'
    template_name = 'book_blog/bookblog_create.html'


class BookDeleteView(generic.DeleteView):
    model = BookBlog
    context_object_name = 'book'
    success_url = reverse_lazy('book_blog:bookblog_list')
    template_name = 'book_blog/bookblog_delete.html'



# def book_list_view(request):
#     books = BookBlog.objects.filter(status='pub').order_by('-datetime_modified')
#     context = {'books': books}
#     return render(request, 'book_blog/bookblog_list.html', context)


# def book_detail_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#
#     context = {'book': book}
#     return render(request, 'book_blog/bookblog_detail.html', context)

# def book_create_view(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book_blog:bookblog_list')
#     else:
#         form = BookForm()
#
#     context = {'form': form}
#     return render(request, 'book_blog/bookblog_create.html', context)


# def book_update_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#     form = BookForm(instance=book, data=request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('book_blog:bookblog_list')
#
#     context = {'form': form}
#     return render(request, 'book_blog/bookblog_create.html', context)

# def book_delete_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book_blog:bookblog_list')
#
#     context = {'book': book}
#     return render(request, 'book_blog/bookblog_delete.html', context)

