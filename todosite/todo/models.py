from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=250)
    is_done = models.BooleanField(default=False)