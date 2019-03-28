from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.TasksListAPIView.as_view()),
    path('mytasks', views.MyTasksAPIView.as_view()),
    path('tasks/<int:pk>', views.TaskDetailAPIView.as_view()),
    path('tasks/update/<int:pk>', views.TaskUpdateAPIView.as_view()),
    path('tasks/create', views.TaskCreateAPIView.as_view(), name='create')
]

urlpatterns = format_suffix_patterns(urlpatterns)