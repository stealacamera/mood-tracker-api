from django.db.models import Avg, Count
from django.db.models.functions import TruncYear, Round
from rest_framework import viewsets, views
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django_filters.rest_framework import DjangoFilterBackend
from datetime import date, timedelta

from .models import MoodEntry
from users_app.models import Profile
from .serializers import MoodEntrySerializer
from .filters import MoodEntryFilter
from .pagination import MoodEntryPagination


# CRUD methods for mood entries of current logged in user 
# or all users if logged in as admin
#
# Updates current user's profile when creating entry
class MoodEntryDisplay(viewsets.ModelViewSet):
    serializer_class = MoodEntrySerializer
    
    filter_backends = [DjangoFilterBackend]
    filterset_class = MoodEntryFilter
    
    pagination_class = MoodEntryPagination
    
    def get_queryset(self):
        if not self.request.user.is_superuser:
            return MoodEntry.objects.filter(user=self.request.user)
        
        return MoodEntry.objects.all()
    
    def perform_create(self, serializer):
        user_entries = MoodEntry.objects.filter(user=self.request.user)
        user_profile = Profile.objects.get(user=self.request.user)
        yesterday_date = date.today() - timedelta(days=1)
        
        if user_entries.filter(created_on=date.today()).exists():
            pass
        elif user_entries.filter(created_on=yesterday_date).exists() or user_entries.count() == 0:
            user_profile.current_streak += 1
        else:
            user_profile.current_streak = 0
        
        if user_profile.current_streak > user_profile.best_streak:
            user_profile.best_streak = user_profile.current_streak
        
        user_profile.save()
        serializer.save()


# Shows no. of entires & average mood per year based on logged in user's entries
# or all users entries if logged in as admin
class AnnualSummariesList(views.APIView):
    def get(self, request):
        current_user = self.request.user
        user_entries = MoodEntry.objects.all()
        
        if not current_user.is_superuser:
            user_entries = user_entries.filter(user=current_user)
        
        entries = user_entries.annotate(year=TruncYear('date')).values('year') \
                                .annotate(num_of_entries=Count('created_on'), avg_mood=Round(Avg('mood'), 2))
        
        return Response(list(entries), status=HTTP_200_OK)
