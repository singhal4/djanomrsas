# Generated by Django 2.2.1 on 2019-08-23 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_auto_20190809_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teststructure',
            name='idTestStructure',
            field=models.CharField(max_length=64),
        ),
    ]
