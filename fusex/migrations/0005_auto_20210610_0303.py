# Generated by Django 3.2.4 on 2021-06-10 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fusex', '0004_auto_20210209_1106'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beneficiario',
            options={'ordering': ('nome',)},
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]