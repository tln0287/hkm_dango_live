# Generated by Django 4.0 on 2022-01-02 05:46

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Festivals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('event_image', models.ImageField(upload_to='events/')),
            ],
            options={
                'verbose_name_plural': 'Festivals',
            },
        ),
    ]