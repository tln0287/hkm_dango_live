# Generated by Django 4.0 on 2022-01-06 03:51

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('SrilaPrabhupada', '0003_remove_srilaprabhupada_title_delete_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Archana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('image', models.ImageField(null=True, upload_to='archana/')),
            ],
            options={
                'verbose_name_plural': 'Archana',
            },
        ),
        migrations.CreateModel(
            name='Bhajans',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('image', models.ImageField(null=True, upload_to='bhajans/')),
            ],
            options={
                'verbose_name_plural': 'Bhajans',
            },
        ),
        migrations.CreateModel(
            name='Biography',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('image', models.ImageField(null=True, upload_to='biography/')),
            ],
            options={
                'verbose_name_plural': 'Biography',
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('image', models.ImageField(null=True, upload_to='books/')),
            ],
            options={
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Lectures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=500, null=True)),
                ('content', tinymce.models.HTMLField(default='<p>Add content</p>')),
                ('image', models.ImageField(null=True, upload_to='lectures/')),
            ],
            options={
                'verbose_name_plural': 'Lectures',
            },
        ),
    ]