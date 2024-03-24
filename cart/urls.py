from django.urls import path
from .views import CartAddView, CartRemoveView, CartDetailView

app_name = 'cart'

urlpatterns = [
    path('', CartDetailView.as_view(), name='cart-detail'),
    path('add/<int:item_id>', CartAddView.as_view(), name='cart-add'),
    path('remove/<int:item_id>', CartRemoveView.as_view(), name='cart-remove')
]
