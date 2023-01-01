from django import forms
from .models import Book, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'book_name',
            'book_author',
            'translator',
            'publisher',
            'publication_year',
            'description',
            'price',
            'book_page',
            'author',
            'status',
            'subject',
            'image',
        ]
        # widgets = {'description': forms.Textarea(attrs={'col': 120, 'row': 10})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'score', 'recommend',]

