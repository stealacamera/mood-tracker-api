from email.mime import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodEntryDisplay, AnnualSummariesList

router = DefaultRouter()
router.register(r'', MoodEntryDisplay, basename='mood')

urlpatterns = [
    path('', include(router.urls)),
    path('summary/annual/', AnnualSummariesList.as_view(), name='summary-list'),
]