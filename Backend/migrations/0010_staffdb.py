# Generated by Django 5.0.6 on 2024-07-05 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0009_rename_hoteldb_roomnamedb'),
    ]

    operations = [
        migrations.CreateModel(
            name='staffdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('STAFFNAME', models.CharField(blank=True, max_length=100, null=True)),
                ('STAFFDESIGNATION', models.CharField(blank=True, max_length=100, null=True)),
                ('STAFFACEBOOK', models.CharField(blank=True, max_length=100, null=True)),
                ('STAFFINSTA', models.CharField(blank=True, max_length=100, null=True)),
                ('STAFFIMAGE', models.ImageField(blank=True, null=True, upload_to='staffimage')),
            ],
        ),
    ]
