from django.http import HttpResponse
from django.shortcuts import render
import django_filters.rest_framework

from rest_framework import filters
from rest_framework.generics import (CreateAPIView, ListAPIView,
                                     RetrieveAPIView, RetrieveUpdateAPIView,
                                     )
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)

from .models import Tasks
from .pagination import TaskPagination
from .permissions import IsOwner
from .serializers import (TaskCreateSerializer, TaskDetailSerializer,
                          TasksSerializer, TaskUpdateSerializer)

# Create your views here.


class TasksListAPIView(ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TasksSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('name', 'description')
    ordering_fields = ('name', 'user', 'status', 'deadline')
    pagination_class = TaskPagination


class MyTasksAPIView(ListAPIView):
    serializer_class = TasksSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(user=user)


class TaskDetailAPIView(RetrieveAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskDetailSerializer


class TaskCreateAPIView(CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TaskUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskUpdateSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwner)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
