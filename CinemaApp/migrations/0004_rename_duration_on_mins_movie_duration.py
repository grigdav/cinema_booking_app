# Generated by Django 4.2.16 on 2024-09-07 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CinemaApp', '0003_remove_movie_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='duration_on_mins',
            new_name='duration',
        ),
    ]
