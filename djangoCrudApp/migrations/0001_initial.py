# Generated by Django 2.2.3 on 2019-07-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=35)),
                ('content', models.CharField(max_length=35)),
                ('created_on', models.DateTimeField(verbose_name='date created')),
            ],
        ),
    ]
