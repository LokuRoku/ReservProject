# Generated by Django 2.2.2 on 2019-06-06 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actualsong',
            name='selection_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время выбора'),
        ),
    ]
