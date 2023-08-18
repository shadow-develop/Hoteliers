from django.urls import path

from hoteliers.web.views import LandingPageView, about_page, HotelDetailsView, HotelCreateView, HomePage, \
    HotelDeleteView, HotelEditView, HotelGalleryView ,HotelProfileView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing page'),
    path('home/<int:pk>', HomePage.as_view(), name='user home'),
    path('about/', about_page, name='about'),

    path('hotel/create/<int:pk>/', HotelCreateView.as_view(), name='hotel create'),
    path('hotel/details/<int:pk>/', HotelDetailsView.as_view(), name='hotel details'),
    path('hotel/edit/<int:pk>/', HotelEditView.as_view(), name='hotel edit'),
    path('hotel/delete/<int:pk>/', HotelDeleteView.as_view(), name='hotel delete'),
    path('hotel/gallery/<int:pk>/', HotelGalleryView.as_view(), name='hotel gallery'),
]
