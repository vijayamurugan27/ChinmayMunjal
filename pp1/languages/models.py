from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length= 250)
    description = models.TextField()
    def __str__(self):
        return self.name