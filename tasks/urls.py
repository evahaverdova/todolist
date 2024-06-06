from django.urls import path
from .views import task_list, task_create, task_complete, task_edit, task_delete

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('complete/<int:task_id>/', task_complete, name='task_complete'),
    path('edit/<int:task_id>/', task_edit, name='task_edit'),
    path('delete/<int:task_id>/', task_delete, name='task_delete'),
]
