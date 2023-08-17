from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from hoteliers.common.views_mixins import RedirectToHome, SuccessMessageMixin
from hoteliers.web.forms import HotelCreateForm, HotelDeleteForm, HotelEditForm
from hoteliers.web.models import Hotel

UserModel = get_user_model()


class LandingPageView(RedirectToHome, views.TemplateView):
    template_name = 'unauth/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


class HomePage(auth_mixins.LoginRequiredMixin, views.ListView):
    model = Hotel
    template_name = 'accounts/user_home.html'
    context_object_name = 'hotel'
    object = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_pk'] = self.request.user.pk
        context['user'] = self.request.user
        hotels = list(Hotel.objects.filter(owner_id=context['user_pk']))
        context.update({'hotels': hotels, })
        return context


class HotelCreateView(SuccessMessageMixin, views.CreateView):
    form_class = HotelCreateForm
    template_name = 'web/hotel_create.html'
    success_message = 'Congratulations! The hotel %(name)s was just added to your hotels list'

    def get_success_url(self):
        return reverse_lazy('hotel details', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class HotelDetailsView(views.DetailView):
    model = Hotel
    template_name = 'web/hotel_details.html'
    context_object_name = 'hotel'


class HotelEditView(SuccessMessageMixin, views.UpdateView):
    model = Hotel
    template_name = 'web/hotel_edit.html'
    form_class = HotelEditForm
    success_message = "%(name)s details updated successfully!"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('hotel details', kwargs={'pk': self.object.pk})


class HotelDeleteView(SuccessMessageMixin, views.DeleteView):
    model = Hotel
    form_class = HotelDeleteForm
    template_name = 'web/hotel_delete.html'
    success_message = 'Hotel deleted successfully!'

    def get_success_url(self):
        return reverse_lazy('user home', kwargs={'pk': self.request.user.pk})


def about_page(request):
    return render(request, 'unauth/about_page.html')


class HotelProfileView(views.TemplateView):
    template_name = 'web/hotel_profile.html'


class HotelGalleryView(views.ListView):
    model = Hotel
    template_name = 'web/hotel_gallery.html'
    context_object_name = 'hotel'
    object = UserModel

