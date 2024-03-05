from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from item.views import ItemListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, ItemSearchListView

app_name = 'item'

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/update', ItemUpdateView.as_view(), name='item-update'),
    path('item/create', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='item-delete'),
    path('search/', ItemSearchListView.as_view(), name='item-search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)