# Generated by Django 4.2.5 on 2023-09-08 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0005_alter_songalbum_track_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songalbum',
            name='track_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
