# Generated by Django 3.2.18 on 2023-03-22 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_alter_task_due_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
