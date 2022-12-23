from .cart import Cart


def cart_processor(request):
    return {'cart_processor': Cart(request)}
