# Generated by Django 5.1 on 2024-09-07 10:10

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_alter_event_details_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event_details',
            name='event_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event_details',
            name='event_date',
            field=models.DateField(),
        ),
    ]
