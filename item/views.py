from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item


class HomeView(ListView):
    model = Item
    template_name = 'item/home.html'
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/item.html'
    context_object_name = 'item'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'price', 'description', 'photo', 'category', 'owner']

    def get_success_url(self):
        return reverse('item:item-detail', kwargs={'pk': self.object.pk})


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'price', 'description', 'photo', 'category', 'owner']

    def get_success_url(self):
        return reverse('item:item-detail', kwargs={'pk': self.object.pk})

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != self.request.user:
            raise Http404('You are not the owner of this item')
        return super().dispatch(request, *args, **kwargs)


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    context_object_name = 'item'
    success_url = reverse_lazy('item:home')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != self.request.user:
            raise Http404('You are not the owner of this item')
        return super().dispatch(request, *args, **kwargs)


