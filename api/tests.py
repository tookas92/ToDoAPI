from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Tasks

# Create your tests here.


class ModelTestCase(TestCase):
    
    def create_task(self, name="only a test", user=User.objects.get(id=1), status='n',
                    deadline=timezone.now() + timezone.timedelta(days=7),
                    description="test case"):
        return Tasks.objects.create(name="only a test", user=user, status='n',
                    deadline=timezone.now() + timezone.timedelta(days=7),
                    description="test case")

    def test_task_creation(self):
        w = self.create_task()
        self.assertTrue(isinstance(w, Tasks))


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        User.objects.create_user(username="test", password="test123")
        user = User.objects.get(username="test")
        self.client.login(username="test", password="test123")
        self.taskdata = {"name": "Test task","user": user.id, "status": "n",
                         "deadline": timezone.now() + timezone.timedelta(days=2), "description": "Test"}
        self.response = self.client.post(
            reverse('create'),
            self.taskdata,
            format="json")


    def test_api_can_create_task(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)