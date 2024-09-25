# Generated by Django 5.0.6 on 2024-07-13 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0010_staffdb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomnamedb',
            name='ROOMIMAGE',
        ),
        migrations.AddField(
            model_name='roomnamedb',
            name='ROOMIMAGE1',
            field=models.ImageField(blank=True, null=True, upload_to='roomimage1'),
        ),
        migrations.AddField(
            model_name='roomnamedb',
            name='ROOMIMAGE2',
            field=models.ImageField(blank=True, null=True, upload_to='roomimage2'),
        ),
    ]