# Generated by Django 3.0 on 2020-05-29 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0015_auto_20200529_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='like_count',
            field=models.IntegerField(default=0),
        ),
    ]
