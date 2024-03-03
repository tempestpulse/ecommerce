from django.contrib.auth import login, logout
from django.db import models
from django.http import Http404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView, DeleteView
from django.views import View

from account.forms import CustomUserCreationForm
from account.models import Profile, Follower
from item.models import Item


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('item:home')


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('item:home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('item:home')
        return super(RegisterView, self).get(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('item:home')


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'account/profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.object
        item_list = Item.objects.filter(owner=profile.user)
        context['item_list'] = item_list

        user = profile.user
        follower_count = Follower.follower_count(user)
        following_count = Follower.following_count(user)
        context['follower_count'] = follower_count
        context['following_count'] = following_count

        return context


class ProfileDeleteView(DeleteView):
    model = Profile
    context_object_name = 'profile'
    success_url = reverse_lazy('item:home')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().user != request.user:
            raise Http404("You are not the owner of the profile")
        return super().dispatch(request, *args, **kwargs)


class FollowUnfollowView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        follow_status = Follower.objects.filter(user=user, followed_by=request.user).exists()

        if request.user == user:
            return redirect('account:profile-detail', pk=user.profile.pk)

        if follow_status:
            Follower.objects.filter(user=user, followed_by=request.user).delete()
        else:
            Follower.objects.create(user=user, followed_by=request.user)
        return redirect('account:profile-detail', pk=user.profile.pk)




