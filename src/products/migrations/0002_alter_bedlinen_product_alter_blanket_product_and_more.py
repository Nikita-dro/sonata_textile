# Generated by Django 4.2.7 on 2023-12-09 14:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bedlinen",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bed_linens",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="blanket",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="blankets",
                to="products.product",
            ),
        ),
        migrations.AlterField(
            model_name="towel",
            name="product",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="towels",
                to="products.product",
            ),
        ),
    ]
