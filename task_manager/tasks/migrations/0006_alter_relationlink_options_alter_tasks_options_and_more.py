# Generated by Django 4.1.3 on 2022-11-24 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0002_alter_labels_options_alter_labels_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('statuses', '0002_alter_statuses_options_alter_statuses_name'),
        ('tasks', '0005_rename_tag_id_tasks_label'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='relationlink',
            options={},
        ),
        migrations.AlterModelOptions(
            name='tasks',
            options={},
        ),
        migrations.AlterField(
            model_name='tasks',
            name='creator',
            field=models.ForeignKey(blank=True, default=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='description',
            field=models.CharField(default='', max_length=1000, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='label',
            field=models.ManyToManyField(blank=True, through='tasks.RelationLink', to='labels.labels', verbose_name='Меткa'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='performer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='performer', to=settings.AUTH_USER_MODEL, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='statuses.statuses', verbose_name='Статус'),
        ),
    ]
