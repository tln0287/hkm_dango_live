# Generated by Django 3.2.7 on 2022-01-04 14:09

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='SrilaPrabhupada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('timestamp', models.DateTimeField(auto_now=True, verbose_name='Timestamp')),
                ('image', models.ImageField(upload_to='events/')),
                ('event_date', models.DateField(blank=True, null=True)),
                ('title', models.ManyToManyField(related_name='post', to='SrilaPrabhupada.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Our Archana',
            },
        ),
    ]