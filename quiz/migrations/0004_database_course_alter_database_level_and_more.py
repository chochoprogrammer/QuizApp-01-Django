# Generated by Django 4.1.4 on 2022-12-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_database_optionc_database_optiond_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='course',
            field=models.CharField(max_length=7, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='level',
            field=models.CharField(choices=[(None, 'Select LEVEL'), ('100', '100'), ('200', '200'), ('300', '300'), ('400', '400'), ('500', '500')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='database',
            name='school',
            field=models.CharField(choices=[(None, 'Select SCHOOL'), ('SEET', 'SEET'), ('SAAT', 'SAAT'), ('SET', 'SET'), ('SEMS', 'SEMS'), ('SPS', 'SPS'), ('SOC', 'SOC'), ('SOS', 'SOS')], max_length=100, null=True),
        ),
    ]