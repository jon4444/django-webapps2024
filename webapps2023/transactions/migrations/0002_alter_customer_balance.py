# Generated by Django 4.1.6 on 2023-04-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customer",
            name="balance",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
