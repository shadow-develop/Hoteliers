from django.contrib import admin

# Register your models here.
from hoteliers.accounts.models import HoteliersUser


@admin.register(HoteliersUser)
class HoteliersUserAdmin(admin.ModelAdmin):
    list_filter = ('email', 'date_joined', 'is_staff',)