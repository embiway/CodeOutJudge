# Generated by Django 3.0 on 2020-05-30 03:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0017_auto_20200529_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='creation_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='submission',
            name='language_used',
            field=models.TextField(default='C++ (GCC 9.2.0)', max_length=20),
        ),
    ]
