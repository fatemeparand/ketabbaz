from django.urls import path
from . import views

app_name = 'book_blog'

urlpatterns = [
    path('', views.book_list_view, name='bookblog_list'),
    path('<int:book_id>/', views.book_detail_view, name='bookblog_detail'),
]
