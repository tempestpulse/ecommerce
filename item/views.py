from django.db.models import Q
from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item


class ItemListView(ListView):
    model = Item
    template_name = 'item/home.html'
    context_object_name = 'item_list'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/item.html'
    context_object_name = 'item'


class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'price', 'description', 'photo', 'category']

    def get_success_url(self):
        return reverse('item:item-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


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


class ItemSearchListView(ListView):
    model = Item
    context_object_name = 'items'
    template_name = 'item/item_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q', None)
        if query is not None:
            return Item.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return Item.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', None)
        return context
