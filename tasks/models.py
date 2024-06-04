from django.db import models
from django.conf import settings

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    start_time = models.DateTimeField(null=True, blank=True)  # Aktualizujte názov poľa
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
