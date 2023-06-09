# Generated by Django 4.1.6 on 2023-04-17 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_alter_customer_balance"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomerTransfer",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("enter_your_username", models.CharField(max_length=50, null=True)),
                (
                    "enter_destination_username",
                    models.CharField(max_length=50, null=True),
                ),
                ("enter_amount_to_transfer", models.IntegerField(null=True)),
            ],
        ),
    ]
