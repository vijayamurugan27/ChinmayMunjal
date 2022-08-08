from django.db import models

from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 10)
    content = models.TextField()
    likes = models.ManyToManyField(User, related_name='like', default=None, blank = True)
    slug = models.SlugField(max_length=250,)

    def get_absolute_url(self):
        return reverse('app1:post_single', args=[self.slug])

    def __str__(self):
        return self.title
