# Generated by Django 3.2.18 on 2023-04-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0016_alter_task_progress'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_shared',
            field=models.BooleanField(default=False),
        ),
    ]
