from django.shortcuts import render
from django.views import generic as views

from hoteliers.common.views_mixins import RedirectToHome


class LandingPageView(RedirectToHome, views.TemplateView):
    template_name = 'unauth/landing_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hide_additional_nav_items'] = True
        return context


def about_page(request):
    return render(request, 'unauth/about_page.html')
