# Generated by Django 5.0.1 on 2024-01-09 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0003_movies_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movies',
            old_name='descr',
            new_name='desc',
        ),
        migrations.AlterField(
            model_name='movies',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
