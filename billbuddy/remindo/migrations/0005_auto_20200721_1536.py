# Generated by Django 3.0 on 2020-07-21 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remindo', '0004_auto_20200721_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminders',
            name='sent',
            field=models.CharField(choices=[('SEN', 'Sent'), ('FOC', 'OutOfCreditException'), ('FID', 'InvalidDestinationException'), ('SCD', 'Scheduled')], max_length=3),
        ),
    ]
