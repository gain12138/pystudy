# Generated by Django 3.0 on 2020-04-11 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200410_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='directors',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='douban_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='douban_votes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='imdb_id',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='languages',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='mins',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='regions',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='storyline',
            field=models.TextField(null=True),
        ),
    ]