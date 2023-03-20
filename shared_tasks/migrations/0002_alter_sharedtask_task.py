# Generated by Django 3.2.18 on 2023-03-20 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0008_alter_task_category'),
        ('shared_tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedtask',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shared_tasks', to='tasks.task'),
        ),
    ]