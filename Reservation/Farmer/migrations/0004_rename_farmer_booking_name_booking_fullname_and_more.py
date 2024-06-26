# Generated by Django 5.0.2 on 2024-05-13 07:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Driver", "0007_driverbooking"),
        ("Farmer", "0003_rename_name_booking_farmer_remove_booking_fullname_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="farmer",
            new_name="name",
        ),
        migrations.AddField(
            model_name="booking",
            name="fullname",
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name="booking",
            name="vehicle",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Driver.vehicle",
            ),
        ),
    ]
