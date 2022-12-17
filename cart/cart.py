from book_store.models import Book


class Cart:
    # initial cart
    def __init__(self, request):
        self.request = request
        self.session = request.session
        cart = self.session.get('cart')

        if not cart:
            cart = self.session['cart'] = {}

        self.cart = cart

    # add to shopping cart
    def add(self, book, quantity=1):
        book_id = str(book.id)

        if book_id not in self.cart:
            self.cart[book_id] = {'quantity': quantity}

        else:
            self.cart[book_id][quantity] += quantity

        self.save()

    def save(self):
        self.session.modified = True

    # Remove from the shopping cart
    def remove(self, book):
        book_id = str(book.id)

        if book_id in self.cart:
            del self.cart[book_id]
            self.save()

    # The ability to loop over books
    def __iter__(self):
        book_ids = self.cart.keys()

        books = Book.objects.filter(id__in=book_ids)
        cart = self.cart.copy()

        for book in books:
            cart[book.id]['book.obj'] = book

        for item in cart.values():
            yield item

    # Number of books
    def __len__(self):
        return len(self.cart.keys())

    # Empty the shopping cart
    def clear(self):
        del self.session['cart']
        self.save()

    def get_total_price(self):
        book_id = self.cart.keys()
        books = Book.objects.filter(id__in=book_id)
        return sum(book.price for book in books)


