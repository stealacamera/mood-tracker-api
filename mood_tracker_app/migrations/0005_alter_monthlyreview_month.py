# Generated by Django 4.1 on 2022-09-01 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0004_monthlyreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monthlyreview',
            name='month',
            field=models.IntegerField(),
        ),
    ]