from django.shortcuts import render, get_object_or_404, redirect
from cart.cart import Cart

from .forms import CartAddItemForm
from item.models import Item


def cart_add(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    form = CartAddItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(item=item, quantity=cd['quantity'], update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, item_id):
    cart = Cart(request)
    item = get_object_or_404(Item, id=item_id)
    cart.remove(item)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddItemForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/cart_detail.html', {'cart': cart})
