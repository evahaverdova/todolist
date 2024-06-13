# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('add_filter/', views.add_filter, name='add_filter'),
    path('delete_filter/', views.delete_filter, name='delete_filter'),
    path('create/', views.task_create, name='task_create'),
    path('complete/<int:task_id>/', views.task_complete, name='task_complete'),
    path('edit/<int:task_id>/', views.task_edit, name='task_edit'),
    path('delete/<int:task_id>/', views.task_delete, name='task_delete'),
]
