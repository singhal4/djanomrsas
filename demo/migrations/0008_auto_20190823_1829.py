# Generated by Django 2.2.1 on 2019-08-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20190823_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testchip',
            old_name='idTC',
            new_name='idTectChip',
        ),
    ]
