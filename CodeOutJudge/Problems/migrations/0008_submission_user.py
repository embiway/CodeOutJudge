# Generated by Django 3.0 on 2020-05-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0007_auto_20200527_1127'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Problems.Profile'),
        ),
    ]