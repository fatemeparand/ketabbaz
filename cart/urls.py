from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail_view, name='cart_detail'),
    path('add/<int:book_id>/', views.add_to_cart_view, name='cart_add'),
    path('remove/<int:book_id>/', views.remove_from_cart, name='cart_remove'),
    path('clear_cart/', views.clear_cart, name='cart_clear'),
]
