# Generated by Django 4.1 on 2022-09-03 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0025_monthlysummary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MonthlySummary',
        ),
    ]
