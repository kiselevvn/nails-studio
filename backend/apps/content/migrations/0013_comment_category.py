# Generated by Django 3.2.10 on 2022-04-26 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0012_gallery_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='category',
            field=models.IntegerField(choices=[(0, 'Сообщение'), (1, 'Курсы')], default=0, verbose_name='Категория отзыва'),
        ),
    ]