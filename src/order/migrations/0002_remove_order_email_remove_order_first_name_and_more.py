# Generated by Django 4.2.7 on 2023-12-10 20:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="email",
        ),
        migrations.RemoveField(
            model_name="order",
            name="first_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="last_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="middle_name",
        ),
        migrations.RemoveField(
            model_name="order",
            name="phone_number",
        ),
    ]
