from django.shortcuts import render, get_object_or_404, redirect
from django.views import View

from cart.cart import Cart
from .forms import CartAddItemForm
from item.models import Item


def cart_add(request, item_id):
    cart = Cart(request)
    cart.add(item_id)

    return redirect('cart:cart-detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    cart.remove(item_id)
    return redirect('cart:cart-detail')


def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
