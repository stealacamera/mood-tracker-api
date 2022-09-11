# Generated by Django 4.1 on 2022-09-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mood_tracker_app', '0027_categories_moodentry_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moodentry',
            name='categories',
        ),
        migrations.AddField(
            model_name='moodentry',
            name='activity',
            field=models.CharField(choices=[('Sports', 'Playing sport(s)'), ('Exercise', 'Doing exercise'), ('Movies', 'Watching movies'), ('Reading', 'Reading'), ('Gaming', 'Playing video games'), ('Drawing', 'Drawing'), ('Other', 'Other')], default='Other', max_length=50),
        ),
        migrations.AddField(
            model_name='moodentry',
            name='social_situation',
            field=models.CharField(choices=[('Myself', 'Myself'), ('Acquaintances', 'Acquaintances'), ('Friends', 'Friends'), ('Family', 'Family'), ('Partner', 'Partner')], default='Myself', max_length=50),
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
