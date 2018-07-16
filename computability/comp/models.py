from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(default="open", max_length=20)
    title = models.CharField(max_length=1000, default="Title here...")
    abstract = models.TextField(max_length=10000, default="Abstract goes here...")
    text = models.TextField(max_length=50000, default="Text goes here...")

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + ":" + self.title


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=50000, default="Text goes here...")

    def __str__(self):
        return self.post.title[:30] + ":" + self.text

