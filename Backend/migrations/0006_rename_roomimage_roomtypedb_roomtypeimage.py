# Generated by Django 5.0.6 on 2024-07-03 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0005_roomtypedb_delete_hoteldb_delete_placedb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomtypedb',
            old_name='ROOMIMAGE',
            new_name='ROOMTYPEIMAGE',
        ),
    ]