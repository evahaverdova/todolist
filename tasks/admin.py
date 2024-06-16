from django.contrib import admin
from .models import Task, TaskStatus

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'start_time', 'end_time', 'user', 'category')  # Prispôsobené podľa modelu
    search_fields = ('title', 'description')

admin.site.register(Task, TaskAdmin)
admin.site.register(TaskStatus)
