# Generated by Django 3.0 on 2020-05-27 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Problems', '0004_problem_submissions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='input_file',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='output_file',
        ),
        migrations.RemoveField(
            model_name='problem',
            name='submissions',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='problems',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='submissions',
        ),
        migrations.AddField(
            model_name='inputfile',
            name='problem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Problems.Problem'),
        ),
        migrations.AddField(
            model_name='outputfile',
            name='problem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Problems.Problem'),
        ),
        migrations.AddField(
            model_name='problem',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Problems.Profile'),
        ),
        migrations.AddField(
            model_name='submission',
            name='problem',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Problems.Problem'),
        ),
    ]
