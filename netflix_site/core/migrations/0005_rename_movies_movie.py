# Generated by Django 5.0.6 on 2024-06-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_movies_image_card_alter_movies_image_cover_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Movies',
            new_name='Movie',
        ),
    ]
