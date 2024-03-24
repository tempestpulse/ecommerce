from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.cart import Cart
from .forms import CartAddItemForm
from item.models import Item


class CartAddView(View):
    def post(self, request, item_id):
        cart = Cart(request)
        item = get_object_or_404(Item, id=item_id)
        cart.add(item)

        return redirect(request, 'cart:cart-detail')


class CartRemoveView(View):
    def get(self, request, item_id):
        cart = Cart(request)
        item = get_object_or_404(Item, id=item_id)
        cart.remove(item)
        return redirect('cart:cart_detail')


class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        total = cart.get_total_price()
        for item in cart:
            item['update_quantity_form'] = CartAddItemForm(initial={'quantity': item['quantity'], 'update': True})
        return render(request, 'cart/cart_detail.html', {'total': total})
