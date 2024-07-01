from django.db import models

# Create your models here.

class Todo(models.Model):
    #Three properties of the model
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title