# Generated by Django 5.0.2 on 2024-05-07 08:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Driver", "0005_vehicle_is_working"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="vehicle",
            name="is_working",
        ),
    ]