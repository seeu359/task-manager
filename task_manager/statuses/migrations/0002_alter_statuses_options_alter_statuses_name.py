# Generated by Django 4.1.3 on 2022-11-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statuses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statuses',
            options={},
        ),
        migrations.AlterField(
            model_name='statuses',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Имя'),
        ),
    ]
