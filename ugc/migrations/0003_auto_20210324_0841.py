# Generated by Django 3.1.7 on 2021-03-24 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ugc', '0002_auto_20210324_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='external_id',
            field=models.PositiveIntegerField(unique=True, verbose_name='Id пользователя в соц сети'),
        ),
    ]
