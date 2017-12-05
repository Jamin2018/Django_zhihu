from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length = 64)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 64)


class Post(models.Model):
    title = models.CharField(max_length=64)
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    u = models.ForeignKey('User',to_field='id')

class comment(models.Model):
    body = models.TextField()
    pub_time = models.DateTimeField(auto_now_add=True)
    p = models.ForeignKey('Post',to_field='id')
    u = models.ForeignKey('User',to_field='id')