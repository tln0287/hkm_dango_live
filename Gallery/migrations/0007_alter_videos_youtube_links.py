# Generated by Django 3.2.7 on 2022-01-24 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0006_alter_videos_youtube_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='youtube_links',
            field=models.CharField(max_length=150),
        ),
    ]