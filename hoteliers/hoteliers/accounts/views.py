from django.contrib.auth import views as auth_views, login, authenticate
from django.http import request, HttpResponseRedirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import generic as views

from hoteliers.accounts.forms import CreateUserForm, LoginUserForm, EditUserForm, DeleteUserForm
from hoteliers.accounts.models import User, HoteliersUser
from hoteliers.common.views_mixins import RedirectToHome, SuccessMessageMixin
from hoteliers.web.models import Hotel


class UserRegisterView(RedirectToHome, views.CreateView):
    form_class = CreateUserForm
    template_name = 'accounts/user_register.html'

    def form_valid(self, form):
        # save the new user first
        form.save()
        messages.info(self.request, f'Congratulations! Your Hoteliers account was created successfully!')
        # get the username and password
        username = self.request.POST['email']
        password = self.request.POST['password1']
        # authenticate user then login
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('user home', kwargs={'pk': self.request.user.pk}))


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


class UserEditView(SuccessMessageMixin, views.UpdateView):
    model = User
    pk = model.pk
    form_class = EditUserForm
    template_name = 'accounts/user_edit.html'
    success_message = "Account details updated successfully!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('user details', kwargs={'pk': self.object.pk})


class UserDeleteView(SuccessMessageMixin, views.DeleteView):
    model = HoteliersUser
    form_class = DeleteUserForm
    template_name = 'accounts/user_delete.html'
    success_message = "Account deleted successfully!"

    def get_success_url(self):
        return reverse_lazy('landing page')
