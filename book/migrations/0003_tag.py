# Generated by Django 5.0.3 on 2024-10-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book", "0002_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
    ]
