# Generated by Django 4.2.6 on 2023-12-01 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_userprofile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.CharField(default='Low', max_length=15),
        ),
    ]
