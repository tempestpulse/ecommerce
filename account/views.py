from django.contrib.auth import login, logout
from django.db import models
from account.forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, DetailView

from account.models import Profile
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
        return context
