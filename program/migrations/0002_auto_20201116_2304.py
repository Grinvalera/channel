# Generated by Django 3.1.3 on 2020-11-16 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='time_program',
            field=models.CharField(max_length=128, verbose_name='Время программы'),
        ),
    ]
