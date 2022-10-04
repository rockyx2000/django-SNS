# Generated by Django 3.2.8 on 2022-10-04 05:55

import boardapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_alter_boardmodel_sns_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='read',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='boardmodel',
            name='sns_image',
            field=models.ImageField(upload_to=boardapp.models.image_directory_path),
        ),
    ]
