# Generated by Django 3.1.4 on 2021-04-28 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unesco', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='site',
            name='justification',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
