
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Tasks

import datetime


class TasksSerializer(ModelSerializer):
    delayed = SerializerMethodField()

    def get_delayed(self, instance):
        if instance.deadline < datetime.date.today() and instance.status == "n":
            return "Yes"
        else:
            return "No"

    class Meta:

        model = Tasks
        fields = [
            'id',
            'name',
            'user',
            'status',
            'delayed'
        ]


class TaskDetailSerializer(ModelSerializer):
    delayed = SerializerMethodField()

    def get_delayed(self, instance):
        if instance.deadline < datetime.date.today() and instance.status == "n":
            return "Yes"
        else:
            return "No"

    class Meta:
        model = Tasks
        fields = [
            'id',
            'name',
            'user',
            'status',
            'deadline',
            'delayed',
            'description'
        ]


class TaskCreateSerializer(ModelSerializer):

    class Meta:
        model = Tasks
        fields = [
            'name',
            'status',
            'deadline',
            'description'
        ]


class TaskUpdateSerializer(ModelSerializer):

    class Meta:
        model = Tasks
        fields = ['status']
