# Generated by Django 4.2.2 on 2023-06-06 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movie", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie", name="utube_link", field=models.URLField(blank=True),
        ),
    ]
