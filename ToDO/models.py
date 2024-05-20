from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class TODO(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    Task = models.CharField(max_length=255)

    def __str__(self):
        return self.Task
