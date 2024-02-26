from django.urls import path

from account.views import RegisterView, CustomLoginView, ProfileDetailView
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>', ProfileDetailView.as_view(), name='profile-detail'),
]