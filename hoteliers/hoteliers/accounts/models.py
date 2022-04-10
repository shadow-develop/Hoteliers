from django.contrib.auth import models as auth_models
from django.db import models

from hoteliers.accounts.managers import HoteliersUserManager


class HoteliersUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = HoteliersUserManager()

# class Manager(models.Model):
#     pass
#
# class Employee(models.Model):
#     pass
