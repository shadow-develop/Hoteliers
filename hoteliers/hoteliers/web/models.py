from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary import models as cloudinary_models

from hoteliers.common.validators import validate_letters_only

UserModel = get_user_model()


class Hotel(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 1
    LOCATION_MAX_LENGTH = 75
    LOCATION_MIN_LENGTH = 2
    STARS_MAX_VALUE = 7

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(NAME_MIN_LENGTH),
            validate_letters_only,
        ),
    )
    stars = models.IntegerField(
        blank=True,
        null=True,
    )

    rooms = models.IntegerField(
        blank=True,
        null=True,
    )

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        validators=(
            MinLengthValidator(LOCATION_MIN_LENGTH),
            validate_letters_only,
        ),
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    photo = models.ImageField(null=True, blank=True, upload_to='photos/')

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ('owner', 'name')


class HotelGalleryPhoto(models.Model):
    photo = models.ImageField(null=True, blank=True, upload_to='photos/')

    owned_by_hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE,
    )
