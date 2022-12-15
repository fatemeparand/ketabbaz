from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Book, Comment
from .forms import BookForm, CommentForm


class BookListView(generic.ListView):
    context_object_name = 'books'
    paginate_by = 12
    template_name = 'book/book_list.html'

    def get_queryset(self):
        return Book.objects.filter(active=True).order_by('-datetime_modified')


class BookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'book/book_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm
        return context


class CommentCreateView(generic.CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user

        book_id = int(self.kwargs['pk'])
        book = get_object_or_404(Book, id=book_id)
        obj.book = book

        return super().form_valid(form)


class BookCreateView(LoginRequiredMixin, generic.CreateView):
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


# def book_detail_view(request, pk):
#     book = get_object_or_404(Book, id=pk)
#
#     if request.method == 'POST':
#         comment_form = CommentForm(data= request.POST)
#         if comment_form.is_valid():
#             new_form = comment_form.save(commit=False)
#             new_form.author = request.user
#             new_form.book = book
#             new_form.save()
#             comment_form = CommentForm()
#
#     else:
#         comment_form = CommentForm()
#
#     context = {'book': book, 'Comment_form': comment_form}
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

