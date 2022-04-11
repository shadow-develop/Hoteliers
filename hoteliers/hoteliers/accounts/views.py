from django.contrib.auth import views as auth_views, login, logout
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from hoteliers.accounts.forms import CreateProfileForm, LoginProfileForm
from hoteliers.accounts.models import User


class UserRegisterView(views.CreateView):
    form_class = CreateProfileForm
    template_name = 'accounts/profile_register.html'
    success_url = reverse_lazy('user home')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = LoginProfileForm
    template_name = 'accounts/profile_login.html'
    success_url = reverse_lazy('user home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class HomePage(auth_views.TemplateView):
    profile = User
    template_name = 'accounts/home.html'
