# Generated by Django 4.1 on 2022-08-31 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='moodentry',
            options={'verbose_name_plural': 'Mood entries'},
        ),
    ]
