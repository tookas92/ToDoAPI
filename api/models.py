from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
# Create your models here.


class Tasks(models.Model):

    name = models.CharField(max_length=100, help_text="Task name")
    user = models.ForeignKey(User, related_name='tasks',
                             on_delete=models.CASCADE)
    STATUS = (
        ("n", "New"),
        ("d", "Done")
    )
    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default="n",
        help_text="Task status"
    )
    deadline = models.DateField(
               default=timezone.now() + timezone.timedelta(days=7))
    description = models.TextField(max_length=800)

    class Meta:
        verbose_name_plural = "Tasks"

    def __str__(self):
        return f"{self.id}/{self.name}/{self.status}/{self.user}"
