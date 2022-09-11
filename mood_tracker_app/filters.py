from django_filters import FilterSet, NumberFilter
from .models import MoodEntry

class MoodEntryFilter(FilterSet):
    month = NumberFilter(field_name='date', lookup_expr='month')
    year = NumberFilter(field_name='date', lookup_expr='year')
    
    class Meta:
        model = MoodEntry
        fields = ['mood', 'social_situation', 'activity', 'month', 'year']