# Generated by Django 4.2.6 on 2023-12-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0019_alter_todo_task_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
