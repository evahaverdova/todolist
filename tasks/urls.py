from django.urls import path
from .views import task_list, task_create, task_complete, task_edit  # Upravený import

urlpatterns = [
    path('', task_list, name='task_list'),
    path('create/', task_create, name='task_create'),
    path('complete/<int:task_id>/', task_complete, name='task_complete'),  # Upravená URL cesta pre označenie úlohy ako splnená
    path('edit/<int:task_id>/', task_edit, name='task_edit'),
]
