# Generated by Django 4.0.3 on 2023-08-03 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_hotel_rooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
