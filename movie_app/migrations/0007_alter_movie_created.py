# Generated by Django 5.1.1 on 2024-10-10 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0006_director_category_movie_created_movie_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
