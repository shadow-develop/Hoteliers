from django.urls import path

from hoteliers.web.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing page'),
]