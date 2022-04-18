from django.urls import path

from hoteliers.web.views import LandingPageView, about_page, HotelDetailsView, HotelCreateView, HomePage

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing page'),
    path('home/<int:pk>', HomePage.as_view(), name='user home'),
    path('about/', about_page, name='about'),

    path('hotel/create/<int:pk>/', HotelCreateView.as_view(), name='hotel create'),
    path('hotel/details/<int:pk>/', HotelDetailsView.as_view(), name='hotel details'),
]