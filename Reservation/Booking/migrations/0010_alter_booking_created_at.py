# Generated by Django 5.0.2 on 2024-05-16 05:40

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Booking", "0009_alter_booking_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
