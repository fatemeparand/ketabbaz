from django.contrib import admin
from .models import Book, Subject, Comment

admin.site.register(Subject)


class CommentsInline(admin.TabularInline):
    model = Comment
    list_display = ['book', 'author', 'score', 'datetime_created', 'active']
    ordering = ('-datetime_created',)
    extra = 1


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'book_author', 'author', 'status', 'datetime_modified', 'active')
    ordering = ('-datetime_modified',)
    inlines = [CommentsInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'author', 'score', 'datetime_created', 'active']
    ordering = ('-datetime_created',)
