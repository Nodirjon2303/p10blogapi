from django.contrib.auth.models import User
from django.db import models




class Category(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}"


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='post', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    views_number = models.BigIntegerField(null=True, default=0) 
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.name}'

