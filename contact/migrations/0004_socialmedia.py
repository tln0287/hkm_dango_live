# Generated by Django 3.2.7 on 2022-01-22 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('link', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'verbose_name_plural': 'Social Media',
            },
        ),
    ]