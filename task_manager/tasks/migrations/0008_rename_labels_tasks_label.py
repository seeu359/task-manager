# Generated by Django 4.1.3 on 2022-11-26 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0007_remove_tasks_label_tasks_labels'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='labels',
            new_name='label',
        ),
    ]
