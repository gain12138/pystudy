# Generated by Django 3.0 on 2020-04-12 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_movie_user_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='user_liked',
        ),
    ]
