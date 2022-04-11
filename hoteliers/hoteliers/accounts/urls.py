from django.contrib.auth.views import LogoutView
from django.urls import path

from hoteliers.accounts.views import UserRegisterView, UserLoginView, HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='user home'),
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path("logout/", LogoutView.as_view(), name="logout"),
]
