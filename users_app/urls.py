from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationView, ProfileView, CurrentProfileView

router = DefaultRouter()
router.register('user-profiles', ProfileView, basename='profile')

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    
    path('profile/', CurrentProfileView.as_view(), name='current-user-profile'),
    path('', include(router.urls)), 
]