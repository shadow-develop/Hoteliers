import os

from django.contrib import admin

# Register your models here.
from hoteliers.accounts.models import HoteliersUser, User


@admin.register(HoteliersUser)
class HoteliersUserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'date_joined', 'is_staff',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_filter = ('first_name', 'gender',)
    api_key =os.getenv('CLOUDINARY_API_KEY')
