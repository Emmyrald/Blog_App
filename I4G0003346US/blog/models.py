from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.ForeignKey(User, default=1, on_delete=models.CASCADE,)
    intro = models.TextField(default='This is a beginner\'s project' )
    slug = models.SlugField()
    Text = models.TextField()
    Created_Date = models.DateTimeField(auto_now_add=True)
    Published_Date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-Published_Date']
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', default=1, on_delete=models.CASCADE, )
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    Created_Date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['Created_Date']






   


