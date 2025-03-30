

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Todo(models.Model):
    """
    Model to store todo items for users.
    """
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='todos')
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-created_at']
