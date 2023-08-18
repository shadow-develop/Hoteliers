import os

from django.contrib import admin

# Register your models here.
from hoteliers.accounts.models import HoteliersUser, User
from hoteliers.web.models import Hotel, HotelGalleryPhoto


@admin.register(HoteliersUser)
class HoteliersUserAdmin(admin.ModelAdmin):
    list_filter = ('date_joined', 'is_staff',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'last_name', 'gender',)
    list_display = ('__str__', 'gender')


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_filter = ('owner_id', 'location', 'stars')
    list_display = ('name', 'location', 'stars')


@admin.register(HotelGalleryPhoto)
class HotelGalleryPhotoAdmin(admin.ModelAdmin):
    pass
