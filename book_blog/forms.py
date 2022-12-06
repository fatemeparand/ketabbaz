from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'book_author', 'description', 'author', 'book_page', 'status']
