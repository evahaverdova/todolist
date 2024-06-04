# myprojekt/urls.py
from django.contrib import admin
from django.urls import path, include
from tasks.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', index, name='index'),
]
