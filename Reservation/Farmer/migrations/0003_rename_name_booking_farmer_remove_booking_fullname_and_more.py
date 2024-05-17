# Generated by Django 5.0.2 on 2024-05-13 07:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Driver", "0007_driverbooking"),
        ("Farmer", "0002_booking_vehicle_type"),
    ]

    operations = [
        migrations.RenameField(
            model_name="booking",
            old_name="name",
            new_name="farmer",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="fullname",
        ),
        migrations.RemoveField(
            model_name="booking",
            name="vehicle_type",
        ),
        migrations.AddField(
            model_name="booking",
            name="date",
            field=models.DateField(blank=True, null=True, verbose_name="วันที่"),
        ),
        migrations.AddField(
            model_name="booking",
            name="time",
            field=models.TimeField(blank=True, null=True, verbose_name="เวลา"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="address",
            field=models.TextField(verbose_name="ที่อยู่"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="details",
            field=models.TextField(verbose_name="รายละเอียด"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="phone",
            field=models.CharField(max_length=15, verbose_name="เบอร์โทร"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="quantity",
            field=models.PositiveIntegerField(verbose_name="จำนวนไร่"),
        ),
        migrations.AlterField(
            model_name="booking",
            name="vehicle",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="Driver.vehicle",
            ),
        ),
    ]
