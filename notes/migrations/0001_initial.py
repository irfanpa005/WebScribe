# Generated by Django 3.2 on 2023-08-04 05:36

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', ckeditor.fields.RichTextField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('is_shared', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('is_shared', models.BooleanField(default=False)),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
