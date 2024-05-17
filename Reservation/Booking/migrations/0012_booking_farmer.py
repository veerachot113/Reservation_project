# Generated by Django 5.0.2 on 2024-05-16 05:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0002_userdriver_userfarmer_delete_userprofile"),
        ("Booking", "0011_remove_booking_farmer"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="farmer",
            field=models.ForeignKey(
                default="",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bookings",
                to="Accounts.userfarmer",
            ),
        ),
    ]