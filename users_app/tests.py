from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

# Testing for registering and logging in a user
class RegisterLoginTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'example',
                'email': 'example@user.com',
                'password': 'pass123',
                'password2': 'pass123'}
               
        self.client.post(reverse('register'), data)
    
    def test_register(self):
        data = {'username': 'example2',
                'email': 'example2@user.com',
                'password': 'pass123',
                'password2': 'pass123'}
               
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_login(self):
        data = {'username': 'example',
                'password': 'pass123'}
               
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# Testing getting the profile of the current logged in user,
# and getting all user profiles as a user & as an admin
class ProfileTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='example', password='pass123')
        
        user_data = {'username': user.username,
                     'password': 'pass123'}
        token = self.client.post(reverse('login'), user_data, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
    
    def test_currentprofile(self):
        response = self.client.get(reverse('current-user-profile'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
    
    def test_userprofiles_user(self):
        response = self.client.get(reverse('profile-list'))
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_userprofiles_admin(self):
        admin_user = User.objects.create_superuser(username='adminuser', password='pass123')

        data = {'username': admin_user.username,
                'password': 'pass123'}
        token_response = self.client.post(reverse('login'), data, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token_response))
        
        response = self.client.get(reverse('profile-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)