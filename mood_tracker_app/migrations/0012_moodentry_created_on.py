# Generated by Django 4.1 on 2022-09-01 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0011_alter_review_avg_mood'),
    ]

    operations = [
        migrations.AddField(
            model_name='moodentry',
            name='created_on',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]