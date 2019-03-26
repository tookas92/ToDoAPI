from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
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