from django.db import models


# Create your models here.
class About(models.Model):
    Content = models.TextField()
    Photo = models.ImageField(upload_to='about')

class Service(models.Model):
    Title = models.CharField(max_length=100)
    Subtext = models.TextField()
    Icon = models.ImageField(upload_to='services')


class Contact(models.Model):
    Email = models.EmailField(max_length=100)
    Subject = models.CharField(max_length=100)
    Message = models.TextField()

