# Generated by Django 5.0.2 on 2024-05-16 12:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Accounts", "0002_userdriver_userfarmer_delete_userprofile"),
        ("Booking", "0020_booking_farmer"),
    ]

    operations = [
        migrations.AddField(
            model_name="booking",
            name="driver",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Accounts.userdriver",
            ),
        ),
        migrations.AlterField(
            model_name="booking",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]