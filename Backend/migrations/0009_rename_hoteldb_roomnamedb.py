# Generated by Django 5.0.6 on 2024-07-04 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0008_alter_hoteldb_roomimage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hoteldb',
            new_name='roomnamedb',
        ),
    ]