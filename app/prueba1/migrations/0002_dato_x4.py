# Generated by Django 4.1.1 on 2022-09-29 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dato',
            name='x4',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
