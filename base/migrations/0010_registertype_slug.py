# Generated by Django 3.1.3 on 2020-12-01 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_auto_20201128_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='registertype',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
