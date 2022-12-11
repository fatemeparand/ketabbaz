from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from .models import Book
from .forms import BookForm


class BookListView(generic.ListView):
    context_object_name = 'books'
    template_name = 'book/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(active=True).order_by('-datetime_modified')


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    form_class = BookForm
    context_object_name = 'form'
    template_name = 'book/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    form_class = BookForm
    context_object_name = 'form'
    template_name = 'book/book_create.html'


class BookDeleteView(generic.DeleteView):
    model = Book
    context_object_name = 'book'
    success_url = reverse_lazy('book_store:book_list')
    template_name = 'book/book_delete.html'



# def book_list_view(request):
#     books = BookBlog.objects.filter(status='pub').order_by('-datetime_modified')
#     context = {'books': books}
#     return render(request, 'book/book_list.html', context)


# def book_detail_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#
#     context = {'book': book}
#     return render(request, 'book/book_detail.html', context)

# def book_create_view(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('book:bookblog_list')
#     else:
#         form = BookForm()
#
#     context = {'form': form}
#     return render(request, 'book/book_create.html', context)


# def book_update_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#     form = BookForm(instance=book, data=request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('book:bookblog_list')
#
#     context = {'form': form}
#     return render(request, 'book/book_create.html', context)

# def book_delete_view(request, book_id):
#     book = get_object_or_404(BookBlog, id=book_id)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book:bookblog_list')
#
#     context = {'book': book}
#     return render(request, 'book/book_delete.html', context)

