# Generated by Django 4.2.5 on 2023-09-07 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog_app', '0003_alter_song_unique_together_remove_song_album_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='song',
            unique_together=set(),
        ),
        migrations.CreateModel(
            name='SongAlbum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_number', models.PositiveIntegerField()),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.album')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_app.song')),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='albums',
            field=models.ManyToManyField(related_name='songs', through='catalog_app.SongAlbum', to='catalog_app.album'),
        ),
    ]
