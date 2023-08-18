# Generated by Django 4.0.3 on 2023-08-17 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_alter_hotel_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='gallery_photos',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='HotelGalleryPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='photos/')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.hotel')),
            ],
        ),
    ]