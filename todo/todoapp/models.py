from django.db import models

# Create your models here.
class Todo(models.Model):
    todo_name = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add = True)
    
    def __str__(self):
        return str(self.todo_name)