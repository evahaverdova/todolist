# tasks/urls.py
from django.urls import path
from .views import task_list, create_task, update_task, delete_task

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', create_task, name='task_create'),
    path('edit/<int:pk>/', update_task, name='task_edit'),
    path('delete/<int:pk>/', delete_task, name='task_delete'),
]
