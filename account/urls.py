from django.urls import path

from account.views import RegisterView, CustomLoginView, ProfileDetailView, ProfileDeleteView, FollowUnfollowView, MyFollowsListView, MyFollowersListView
from account import views

app_name = 'account'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile/<int:pk>/follow', FollowUnfollowView.as_view(), name='follow-unfollow'),
    path('profile/<int:pk>/delete', ProfileDeleteView.as_view(), name='profile-delete'),
    path('follows/', MyFollowsListView.as_view(), name='my-follows'),
    path('followers/', MyFollowersListView.as_view(), name='my-followers')
]