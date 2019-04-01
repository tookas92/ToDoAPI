from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.TasksListAPIView.as_view(), name='index'),
    path('mytasks', views.MyTasksAPIView.as_view(), name="mytasks"),
    path('tasks/<int:pk>', views.TaskDetailAPIView.as_view(), name='details'),
    path('tasks/update/<int:pk>', views.TaskUpdateAPIView.as_view(), name='update'),
    path('tasks/create', views.TaskCreateAPIView.as_view(), name='create')
]

urlpatterns = format_suffix_patterns(urlpatterns)