# Generated by Django 4.1.3 on 2022-11-22 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationlink',
            name='task',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.SET_NULL, to='tasks.tasks'),
        ),
    ]
