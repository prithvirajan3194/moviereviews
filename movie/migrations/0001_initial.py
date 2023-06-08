# Generated by Django 4.2.2 on 2023-06-05 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
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
                ("title", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="movie/images/")),
                ("url", models.URLField(blank=True)),
            ],
        ),
    ]
