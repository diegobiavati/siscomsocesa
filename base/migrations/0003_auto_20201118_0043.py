# Generated by Django 3.1.2 on 2020-11-18 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_qualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='branch',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='divisionsession',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='postgraduation',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='registertype',
            name='activate',
            field=models.BooleanField(default=True),
        ),
    ]
