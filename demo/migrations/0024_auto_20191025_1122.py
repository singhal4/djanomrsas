# Generated by Django 2.2.1 on 2019-10-25 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0023_auto_20191025_1114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocol',
            name='furnace',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
