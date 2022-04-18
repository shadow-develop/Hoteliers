from django.contrib.auth import views as auth_views, login
from django.http import request

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from hoteliers.accounts.forms import CreateUserForm, LoginUserForm, EditUserForm
from hoteliers.accounts.models import User
from hoteliers.common.views_mixins import RedirectToHome
from hoteliers.web.models import Hotel


class UserRegisterView(RedirectToHome, views.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/user_register.html'
    success_url = reverse_lazy('user home')

    def form_valid(self, form):
        result = super().form_valid(form)
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        return reverse_lazy('user home', kwargs={'pk': self.request.user.pk})


class UserDetailsView(views.DetailView):
    model = User
    template_name = 'accounts/user_details.html'
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()

        hotels = list(Hotel.objects.filter(owner_id=self.object.user_id))
        total_hotels_count = len(hotels)

        context.update({
            'hotels': hotels,
            'total_hotels_count': total_hotels_count,
        })
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
        return reverse_lazy('user details', kwargs={'pk': self.object.pk})


