from django.db import models
from django.conf import settings
from datetime import date
from . import input_choices

class MoodEntry(models.Model):    
    mood = models.PositiveIntegerField(choices=input_choices.MOOD_CHOICES, default=3)
    reason = models.TextField(null=True, blank=True)
    social_situation = models.CharField(max_length=50, choices=input_choices.SOCIAL_CHOICES, default=input_choices.MYSELF)
    activity = models.CharField(max_length=50, choices=input_choices.ACTIVITIES_CHOICES, default=input_choices.OTHER)
    
    date = models.DateField(default=date.today)
    created_on = models.DateField(auto_now_add=True, null=True)
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}: {}'.format(self.user.username, self.date)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user', 'date'],
                                    name='unique_date_per_user')
        ]
        
        verbose_name_plural = 'Mood entries'