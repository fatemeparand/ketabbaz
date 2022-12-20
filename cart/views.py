from django.shortcuts import render, get_object_or_404, redirect

from .cart import Cart
from book_store.models import Book
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)

    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)


def add_to_cart_view(request, book_id):
    cart = Cart(request)

    book = get_object_or_404(Book, id=book_id)

    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data

        quantity = cleaned_data['quantity']

        cart.add(book, quantity)

        return redirect('cart:cart_detail')


def remove_from_cart(request, book_id):
    cart = Cart(request)

    book = get_object_or_404(Book, id=book_id)

    cart.remove(book)

    return redirect('cart:cart_detail')



