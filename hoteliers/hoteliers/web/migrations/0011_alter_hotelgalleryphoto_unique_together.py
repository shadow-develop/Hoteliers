# Generated by Django 4.0.3 on 2023-08-18 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_rename_hotel_hotelgalleryphoto_owned_by_hotel'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='hotelgalleryphoto',
            unique_together={('owned_by_hotel', 'photo')},
        ),
    ]
