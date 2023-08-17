from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models
from hoteliers.accounts.managers import HoteliersUserManager
from hoteliers.common.validators import validate_letters_only


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


class User(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    NUMBER_MAX_LENGTH = 16

    MALE = 'Male'
    FEMALE = 'Female'
    OTHER = 'Other'
    DEFAULT_GENDERS_CHOICE = 'Not mentioned'
    GENDERS = [(x, x) for x in (MALE, FEMALE, OTHER)]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_letters_only,
        ),
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_letters_only,
        ),
        blank=True,
        null=True,
    )

    gender = models.CharField(
        max_length=max(len(x) for x, _ in GENDERS),
        choices=GENDERS,
        null=True,
        blank=True,
        default=DEFAULT_GENDERS_CHOICE,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    phone_number = models.CharField(
        max_length=NUMBER_MAX_LENGTH,
        unique=True,
        blank=True,
        null=True,
    )

    photo = models.ImageField(null=True, blank=True, upload_to='photos/')

    user = models.OneToOneField(
        HoteliersUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
