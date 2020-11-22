# Generated by Django 3.1.3 on 2020-11-16 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20201116_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='program_type',
            field=models.CharField(choices=[('News', 'Новости'), ('Serials', 'Сериалы'), ('Films', 'Фильмы'), ('Cartoons', 'Мультфильмы'), ('TV_show', 'Телешоу'), ('NightMusic', 'Ночная музыка')], max_length=128, verbose_name='Тип программы'),
        ),
    ]