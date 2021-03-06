from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone


from rest_framework.test import APIClient
from rest_framework import status


from .models import Tasks


class ModelTestCase(TestCase):

    def create_task(self, user=User.objects.get(id=1)):
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
                         "deadline": (timezone.now() + timezone.timedelta(days=2)).strftime('%Y-%m-%d'),
                         "description": "Test"}
        self.response = self.client.post(
            reverse('create'),
            self.taskdata,
            format="json")

    def test_api_can_create_task(self):

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_task(self):
        task = Tasks.objects.get()
        response = self.client.get(
            reverse('details',
                    kwargs={'pk':task.id}),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertContains(response, task)

    def test_api_can_update_task(self):
        task = Tasks.objects.get()
        change_task = {"status":"d"}
        res = self.client.put(
            reverse('update', kwargs={'pk':task.id}),
            change_task,
            format="json"
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_get_mytasks(self):
        response = self.client.get(
            reverse('mytasks'),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_unauthorized_mytasks(self):
        self.client.logout()
        response = self.client.get(
            reverse('mytasks'),
            format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

