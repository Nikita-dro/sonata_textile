# Generated by Django 4.2.7 on 2023-12-10 20:15

import django.db.models.deletion
import djmoney.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="brand",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="products.brand",
                verbose_name="Бренд",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=djmoney.models.fields.MoneyField(
                decimal_places=2,
                default_currency="UAH",
                max_digits=10,
                verbose_name="Ціна",
            ),
        ),
    ]
