from django.urls import path

from account.views import RegisterView, CustomLoginView

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
]