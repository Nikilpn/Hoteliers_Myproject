# Generated by Django 5.0.6 on 2024-07-18 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_alter_bookingdb_checkin_alter_bookingdb_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdb',
            name='TOTALPRICE',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
