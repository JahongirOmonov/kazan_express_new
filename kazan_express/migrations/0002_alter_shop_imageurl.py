# Generated by Django 4.2.7 on 2024-03-01 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("kazan_express", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shop",
            name="imageUrl",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]