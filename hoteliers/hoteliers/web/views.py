from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins, get_user_model
from hoteliers.common.views_mixins import RedirectToHome
from hoteliers.web.forms import HotelCreateForm
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


class HotelCreateView(views.CreateView):
    form_class = HotelCreateForm
    template_name = 'web/hotel_create.html'

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


def about_page(request):
    return render(request, 'unauth/about_page.html')
