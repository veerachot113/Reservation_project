# Generated by Django 5.0.2 on 2024-05-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Driver", "0008_delete_driverbooking"),
    ]

    operations = [
        migrations.AlterField(
            model_name="vehicle",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="vehicle_images/"),
        ),
    ]
