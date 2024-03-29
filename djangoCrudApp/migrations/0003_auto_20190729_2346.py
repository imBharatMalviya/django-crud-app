# Generated by Django 2.2.3 on 2019-07-29 18:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoCrudApp', '0002_auto_20190728_1826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='posts',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=35, unique=True),
        ),
    ]
