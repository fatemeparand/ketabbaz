from django.urls import path
from . import views

app_name = 'book_blog'

urlpatterns = [
    path('', views.book_list_view, name='bookblog_list'),
]
