# Generated by Django 4.2.5 on 2023-09-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0004_alter_song_unique_together_songalbum_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songalbum',
            name='track_number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
