# Generated by Django 5.0.6 on 2024-06-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_movie_director_alter_movie_genre_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Comedy', 'Comedy'), ('Drama', 'Drama'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Science-Fiction', 'Science Fiction'), ('Fantasy', 'Fantasy')], max_length=50),
        ),
    ]
