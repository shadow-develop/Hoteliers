from django.contrib.auth.views import LogoutView
from django.urls import path

from hoteliers.accounts.views import UserRegisterView, UserLoginView, UserDetailsView, UserEditView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user register'),
    path('login/', UserLoginView.as_view(), name='user login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='user details'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='user edit'),
]
