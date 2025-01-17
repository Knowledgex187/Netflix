# Generated by Django 5.0.6 on 2024-06-21 09:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(verbose_name=255)),
                ('description', models.TextField(verbose_name=255)),
                ('stars', models.CharField(verbose_name=100)),
                ('release_date', models.DateField()),
                ('genre', models.CharField(choices=[('ACTION', 'Action'), ('COMEDY', 'Comedy'), ('DRAMA', 'Drama'), ('HORROR', 'Horror'), ('ROMANCE', 'Romance'), ('SCIENCE_FICTION', 'Science Fiction'), ('FANTASY', 'Fantasy')], verbose_name=100)),
                ('length', models.PositiveIntegerField()),
                ('director', models.CharField(verbose_name=50)),
                ('produced_by', models.CharField(verbose_name=50)),
                ('writers', models.CharField(verbose_name=50)),
                ('image_card', models.ImageField(upload_to='images/')),
                ('image_cover', models.ImageField(upload_to='images/')),
                ('video', models.FileField(upload_to='movie_videos/')),
                ('movie_views', models.IntegerField(default=0)),
            ],
        ),
    ]
