from django.urls import path

from hoteliers.web.views import LandingPageView, about_page

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing page'),
    path('about/', about_page, name='about')
]