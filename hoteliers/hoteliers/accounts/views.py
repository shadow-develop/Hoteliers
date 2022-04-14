from django.contrib.auth import views as auth_views, login, get_user_model
from django.contrib.auth import mixins as auth_mixins
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from hoteliers.accounts.forms import CreateUserForm, LoginUserForm, EditUserForm
from hoteliers.accounts.models import User
from hoteliers.common.views_mixins import RedirectToHome


class UserRegisterView(RedirectToHome, views.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('user home')

    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/user_login.html'
    success_url = reverse_lazy('user home')

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        return super().get_success_url()


class UserDetailsView(views.DetailView):
    model = User
    template_name = 'accounts/user_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        return context


class UserEditView(views.UpdateView):
    model = User
    pk = model.pk
    form_class = EditUserForm
    template_name = 'accounts/user_edit.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user profile', kwargs={'pk': self.object.pk})


class HomePage(auth_mixins.LoginRequiredMixin, auth_views.TemplateView):
    profile = User
    template_name = 'accounts/user_home.html'
