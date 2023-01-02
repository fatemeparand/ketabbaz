from django.urls import path
from . import views

app_name = 'book_store'

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('comment/<int:pk>/', views.CommentCreateView.as_view(), name='comment_create'),
    path('new_book/', views.book_create_view, name='book_create'),
    # path('new_book/', views.BookCreateView.as_view(), name='book_create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='book_update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='book_delete'),
]
