# Generated by Django 2.0 on 2018-01-17 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=255),
        ),
    ]