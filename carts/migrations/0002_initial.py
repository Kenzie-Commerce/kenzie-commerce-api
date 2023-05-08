# Generated by Django 4.2.1 on 2023-05-08 18:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("carts", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.ManyToManyField(related_name="carts", to="products.product"),
        ),
    ]
