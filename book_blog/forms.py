from django import forms
from .models import BookBlog


class BookForm(forms.ModelForm):
    class Meta:
        model = BookBlog
        fields = ['book_name', 'book_author', 'introduction', 'author','book_page', 'status']
