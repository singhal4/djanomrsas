# Generated by Django 2.2.1 on 2019-10-23 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0017_auto_20191023_1529'),
    ]

    operations = [
        migrations.AddField(
            model_name='protocol',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='durationMess',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='endDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='failCriterion',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='furnace',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='maxLeakage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='measurementDefinition',
            field=models.FilePathField(null=True, path=None),
        ),
        migrations.AddField(
            model_name='protocol',
            name='numDUT',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='numStructure',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='probeCard',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='prober',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='proberSetup',
            field=models.FilePathField(null=True, path=None),
        ),
        migrations.AddField(
            model_name='protocol',
            name='readout',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='receiveDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='startDate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='tempChuck',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='tempFurnace',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='protocol',
            name='testType',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='topic',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='protocol',
            name='wafer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='demo.Wafer'),
        ),
        migrations.AlterField(
            model_name='protocol',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
