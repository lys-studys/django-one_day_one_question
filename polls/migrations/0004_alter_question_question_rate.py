# Generated by Django 3.2.6 on 2021-08-28 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20210828_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='question_rate',
            field=models.FloatField(default=0),
        ),
    ]