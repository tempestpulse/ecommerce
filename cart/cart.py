from django.conf import settings
from item.models import Item


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def __iter__(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Item.objects.get(pk=p)

        for item in self.cart.values():
            item['total_price'] = item['product'].price * item['quantity']

            yield item

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self, item_id, quantity=1, update_quantity=False):
        item_id = str(item_id)
        if item_id not in self.cart:
            self.cart[item_id] = {'quantity': 0, 'price': str(Item(id=item_id).price)}
        if update_quantity:
            self.cart[item_id]['quantity'] = quantity
        else:
            self.cart[item_id]['quantity'] += quantity
        self.save()

    def remove(self, item_id):
        item_id = str(item_id)
        if item_id in self.cart:
            self.cart[item_id]['quantity'] -= 1
            if self.cart[item_id]['quantity'] == 0:
                del self.cart[item_id]
            self.save()

    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
