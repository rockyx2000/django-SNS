# Generated by Django 3.2.8 on 2022-10-11 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0003_auto_20221004_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='boardmodel',
            name='good_user',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='good',
            field=models.IntegerField(default=0),
        ),
    ]