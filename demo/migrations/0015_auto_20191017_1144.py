# Generated by Django 2.2.1 on 2019-10-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0014_overview_excel_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='overview',
            name='file_path',
        ),
        migrations.RemoveField(
            model_name='protocol',
            name='file_path',
        ),
        migrations.AddField(
            model_name='protocol',
            name='excel_file',
            field=models.URLField(null=True),
        ),
    ]
