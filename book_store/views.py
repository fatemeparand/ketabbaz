from django.shortcuts import render, redirect
from django.views import generic
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.contrib import messages

from .models import Book, Comment
from .forms import BookForm, CommentForm
from cart.forms import AddToCartForm


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
        context['add_to_cart_form'] = AddToCartForm
        return context


@login_required()
def book_create_view(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.author = request.user
            new_form.save()
            messages.success(request, _('book was created successfully'))
            return redirect('book_store:book_list')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'book/book_create.html', context)


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
    

class BookUpdateView(LoginRequiredMixin, SuccessMessageMixin, UserPassesTestMixin, generic.UpdateView):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    model = Book
    form_class = BookForm
    context_object_name = 'form'
    success_message = _("book was updated successfully")
    template_name = 'book/book_create.html'


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

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


# class BookCreateView(LoginRequiredMixin, SuccessMessageMixin, generic.CreateView):
#     model = Book
#     form_class = BookForm
#     context_object_name = 'form'
#     success_message = _("book was created successfully")
#     template_name = 'book/book_create.html'



# @login_required()
# def book_update_view(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     form = BookForm(instance=book, data=request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('book:book_list')
#
#     context = {'form': form}
#     return render(request, 'book/book_create.html', context)


# @login_required()
# def book_delete_view(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == 'POST':
#         book.delete()
#         return redirect('book:book_list')
#
#     context = {'book': book}
#     return render(request, 'book/book_delete.html', context)

