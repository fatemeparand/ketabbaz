from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.utils.translation import gettext as _

from .cart import Cart
from book_store.models import Book
from .forms import AddToCartForm


def cart_detail_view(request):
    cart = Cart(request)

    for item in cart:
        item['book_update_quantity_form'] = AddToCartForm(initial={
            'quantity': item['quantity'],
            'inplace': True,
        })

    context = {'cart': cart}
    return render(request, 'cart/cart_detail.html', context)


@require_POST
def add_to_cart_view(request, book_id):
    cart = Cart(request)

    book = get_object_or_404(Book, id=book_id)

    form = AddToCartForm(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data

        quantity = cleaned_data['quantity']

        cart.add(book, quantity, replace_current_quantity=cleaned_data['inplace'])

        return redirect('book_store:book_detail', book.id)


def remove_from_cart(request, book_id):
    cart = Cart(request)

    book = get_object_or_404(Book, id=book_id)

    cart.remove(book)

    return redirect('cart:cart_detail')


@require_POST
def clear_cart(request):
    cart = Cart(request)
    if len(cart):
        cart.clear()
        messages.success(request, _('All products successfully removed from your cart.'))

    else:
        messages.warning(request, _('Your cart is already empty'))

    return redirect('cart:cart_detail')
