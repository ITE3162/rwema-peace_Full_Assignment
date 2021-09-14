from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
    Title = models.CharField(max_length=100)
    Genre = models.CharField(max_length=50)
    Description = models.TextField()
    Poster = models.ImageField(upload_to='posters')
    Release = models.DateField()
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_at',)
