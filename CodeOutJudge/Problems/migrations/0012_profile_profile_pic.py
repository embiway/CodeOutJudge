# Generated by Django 3.0 on 2020-05-28 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0011_auto_20200528_0212'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(null=True, upload_to='profile_pics'),
        ),
    ]
