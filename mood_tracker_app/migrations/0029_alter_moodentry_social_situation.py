# Generated by Django 4.1 on 2022-09-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0028_remove_moodentry_categories_moodentry_activity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moodentry',
            name='social_situation',
            field=models.CharField(choices=[('By myself', 'By myself'), ('With acquaintances', 'With acquaintances'), ('With friends', 'With friends'), ('With family', 'With family'), ('With partner', 'With partner')], default='By myself', max_length=50),
        ),
    ]
