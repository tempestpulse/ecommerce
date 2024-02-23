from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from item.views import HomeView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

app_name = 'item'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('item/<int:pk>/update', ItemUpdateView.as_view(), name='item-update'),
    path('item/create', ItemCreateView.as_view(), name='item-create'),
    path('item/<int:pk>/delete', ItemDeleteView.as_view(), name='item-delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)