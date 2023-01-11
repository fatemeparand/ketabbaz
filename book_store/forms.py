from django import forms
from django.utils.translation import gettext as _
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
            'status',
            'subject',
            'image',
        ]
        widgets = {'description': forms.Textarea(attrs={'cols': 120})}

    # def clean(self):
    #     try:
    #         Book.objects.get(book_name=self.cleaned_data['book_name'],
    #                          book_author=self.cleaned_data['book_author'],
    #                          translator=self.cleaned_data['translator'],
    #                          publisher=self.cleaned_data['publisher'], )
    #
    #         raise forms.ValidationError(_('This book has already been saved'))
    #     except Book.DoesNotExist:
    #         return self.cleaned_data


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'score', 'recommend', ]
