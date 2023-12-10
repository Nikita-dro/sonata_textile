# Generated by Django 4.2.7 on 2023-12-09 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0004_alter_bedlinen_options_alter_bedspread_options_and_more"),
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cartitem",
            name="added_at",
        ),
        migrations.AlterField(
            model_name="cartitem",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="products.product",
                verbose_name="Товар",
            ),
        ),
    ]