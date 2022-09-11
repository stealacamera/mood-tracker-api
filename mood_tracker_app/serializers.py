from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import MoodEntry

class MoodEntrySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())        
    
    class Meta:
        model = MoodEntry
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(queryset=MoodEntry.objects.all(),
                                    fields=['user', 'date'],
                                    message='You can only create one entry for a given date.')
        ]