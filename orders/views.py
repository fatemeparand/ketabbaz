from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import OrderForm
from .models import OrderItem
from cart.cart import Cart


@login_required
def order_create_view(request):
    order_form = OrderForm()
    cart = Cart(request)

    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                book = item['book_obj']

                OrderItem.objects.create(
                    order=order_obj,
                    book=book,
                    quantity=item['quantity'],
                    price=book.price,
                )
            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name

            request.user.save()

    context = {'form': order_form}
    return render(request, 'orders/order_create.html', context)
