# Generated by Django 4.1 on 2022-09-01 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0018_alter_review_avg_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='avg_mood',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
