# Generated by Django 3.0 on 2020-05-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0005_auto_20200527_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='user',
        ),
        migrations.AddField(
            model_name='problem',
            name='user',
            field=models.ManyToManyField(to='Problems.Profile'),
        ),
    ]