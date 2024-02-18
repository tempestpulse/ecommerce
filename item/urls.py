from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from item.views import HomeView, ItemDetailView

app_name = 'item'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', ItemDetailView.as_view(), name='item-detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)