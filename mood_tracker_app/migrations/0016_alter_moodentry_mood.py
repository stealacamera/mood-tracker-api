# Generated by Django 4.1 on 2022-09-01 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0015_alter_review_avg_mood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='mood',
            field=models.IntegerField(choices=[(5, 'Feeling great!'), (4, 'Feeling good'), (3, 'Not the best, not the worst'), (2, 'Feeling the blues'), (1, 'Feeling dreadful')], default=3),
        ),
    ]
