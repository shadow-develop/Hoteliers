# Generated by Django 4.0.3 on 2022-04-15 12:25

import cloudinary.models
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import hoteliers.common.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1), hoteliers.common.validators.validate_letters_only])),
                ('stars', models.IntegerField()),
                ('location', models.CharField(max_length=75, validators=[django.core.validators.MinLengthValidator(2), hoteliers.common.validators.validate_letters_only])),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
