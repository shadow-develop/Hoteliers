from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('hoteliers.accounts.urls')),
    path('', include('hoteliers.web.urls')),
]
