# Generated by Django 3.2.18 on 2023-03-23 16:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0011_alter_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='shared_to',
            field=models.ManyToManyField(related_name='sharing', to=settings.AUTH_USER_MODEL),
        ),
    ]
