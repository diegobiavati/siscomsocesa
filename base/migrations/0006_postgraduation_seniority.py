# Generated by Django 3.1.3 on 2020-11-21 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_auto_20201118_0205'),
    ]

    operations = [
        migrations.AddField(
            model_name='postgraduation',
            name='seniority',
            field=models.ManyToManyField(blank=True, related_name='_postgraduation_seniority_+', to='base.PostGraduation'),
        ),
    ]
