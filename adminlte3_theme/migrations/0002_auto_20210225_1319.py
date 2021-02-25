# Generated by Django 3.1.7 on 2021-02-25 08:19

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminlte3_theme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='confrence',
            name='city',
        ),
        migrations.RemoveField(
            model_name='confrence',
            name='name',
        ),
        migrations.RemoveField(
            model_name='confrence',
            name='roll',
        ),
        migrations.AddField(
            model_name='confrence',
            name='confrence_ID',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='confrence',
            name='confrence_Overview',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confrence',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confrence',
            name='register',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confrence',
            name='travel_information',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='confrence',
            name='venu',
            field=models.CharField(default='', max_length=50),
        ),
    ]
