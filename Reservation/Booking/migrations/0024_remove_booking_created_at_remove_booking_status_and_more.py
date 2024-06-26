# Generated by Django 5.0.2 on 2024-05-19 18:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Booking", "0023_remove_booking_driver_booking_farmer_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="booking",
            name="created_at",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="status",
        ),
        migrations.AddField(
            model_name="booking",
            name="request_responded_by",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="booking",
            name="request_status",
            field=models.CharField(default="Pending", max_length=30),
        ),
    ]
