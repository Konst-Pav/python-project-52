# Generated by Django 4.2.6 on 2024-01-31 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0001_initial'),
        ('task', '0002_alter_task_author_alter_task_executor'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='labels',
            field=models.ManyToManyField(to='label.label'),
        ),
    ]
