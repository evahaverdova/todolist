# tasks/models.py
from django.db import models
from django.conf import settings

class TaskStatus(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)  # Pridanie end_time
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.ManyToManyField(TaskStatus)
    category = models.CharField(max_length=100, null=True, blank=True)  # Pridanie category

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.status.filter(name='all').exists():
            all_status = TaskStatus.objects.get_or_create(name='all')[0]
            self.status.add(all_status)

    def __str__(self):
        return self.title
