# Generated by Django 4.0.4 on 2022-05-17 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csvapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='password',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='customer',
            name='password1',
            field=models.CharField(max_length=100),
        ),
    ]
