# Generated by Django 4.2.6 on 2024-03-07 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('task', '0003_task_labels'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to='status.status',
            ),
        ),
    ]
