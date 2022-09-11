from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser

from .serializers import RegistrationSerializer, UserSerializer


# Registers user and returns their username & JWT tokens
class RegistrationView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):        
        serializer = RegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
    
        tokens = {'refresh': str(refresh),
                  'access': str(refresh.access_token)}
        
        data = {'username': user.username,
                'tokens': tokens}
        
        return Response(data, status=status.HTTP_201_CREATED)

# Gets the profile of the current logged in user
class CurrentProfileView(APIView):    
    def get(self, request):
        serialized = UserSerializer(request.user)
        return Response(serialized.data)

# Gets the profiles of all the registered users
# Admin-accessible only
class ProfileView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.all().select_related('profile')