from django.urls import path
from . import views

app_name = 'book_blog'

urlpatterns = [
    path('', views.BookListView.as_view(), name='bookblog_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='bookblog_detail'),
    path('new_book/', views.BookCreateView.as_view(), name='bookblog_create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='bookblog_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='bookblog_delete'),
]
