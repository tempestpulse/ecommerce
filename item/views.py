from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'item/home.html'
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/item.html'
    context_object_name = 'item'
