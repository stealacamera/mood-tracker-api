from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

# Testing for creating (with & without the same date, between the same and different users),
# retrieving, listing, updating, deleting a mood entry
class MoodEntryDisplayTestCase(APITestCase):
    def setUp(self):
        user = User.objects.create_user(username='example', password='pass123')
        
        user_data = {'username': user.username,
                     'password': 'pass123'}
        token = self.client.post(reverse('login'), user_data, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token))
        
        entry_data = {'mood': 3,
                      'reason': 'message input',
                      'date': '2020-10-25'}
        self.moodentry = self.client.post(reverse('mood-list'), entry_data).data
    
    def test_entry_create(self):
        entry1 = {'mood': 4,
                  'date': '2022-05-08'}
        entry2 = {'mood': 2,
                  'reason': 'message input',
                  'date': '2022-05-08'}
        
        response1 = self.client.post(reverse('mood-list'), entry1)
        self.assertEqual(response1.status_code, status.HTTP_201_CREATED)
        
        response2 = self.client.post(reverse('mood-list'), entry2)
        self.assertEqual(response2.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_entry_create_differentusers(self):
        user2 = User.objects.create_user(username='example2', password='pass123')
        
        user2_data = {'username': user2.username,
                      'password': 'pass123'}
        token2 = self.client.post(reverse('login'), user2_data, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token2))
        
        entry_data = {'mood': 3,
                      'reason': 'message input',
                      'date': '2020-10-25'}
        response = self.client.post(reverse('mood-list'), entry_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_entry_get(self):
        response = self.client.get(reverse('mood-detail', args=(self.moodentry['id'],)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_entry_list(self):
        response = self.client.get(reverse('mood-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_entry_update(self):
        entry_data = {'activity': 'Reading'}
        
        response = self.client.patch(reverse('mood-detail', args=(self.moodentry['id'],)), entry_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_entry_delete(self):
        response = self.client.delete(reverse('mood-detail', args=(self.moodentry['id'],)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


# Testing for getting the annual summary as a user and as an admin
class AnnualSummaryTestCase(APITestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='example', password='pass123')
        user1_data = {'username': user1.username,
                      'password': 'pass123'}
        token1 = self.client.post(reverse('login'), user1_data, format='json').data['access']
        
        user2 = User.objects.create_user(username='example2', password='pass123')
        user_data2 = {'username': user2.username,
                      'password': 'pass123'}
        token2 = self.client.post(reverse('login'), user_data2, format='json').data['access']
        
        # user1 mood entry
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token1))
        
        entry_data = {'mood': 3,
                      'reason': 'message input',
                      'date': '2020-10-25'}
        self.client.post(reverse('mood-list'), entry_data)
        
        # user2 mood entry
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token2))
        
        entry_data = {'mood': 3,
                      'reason': 'message input',
                      'date': '2020-10-25'}
        self.client.post(reverse('mood-list'), entry_data)
        
    def test_summary_user(self):        
        response = self.client.get(reverse('summary-list'))
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['num_of_entries'], 1)
       
    def test_summary_admin(self):
        self.admin_user = User.objects.create_superuser(username='adminuser', password='pass123')
        
        data = {'username': 'adminuser',
                'password': 'pass123'}
        token_response = self.client.post(reverse('login'), data, format='json').data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {}'.format(token_response))
        
        response = self.client.get(reverse('summary-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['num_of_entries'], 2)