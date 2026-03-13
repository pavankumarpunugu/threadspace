
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField(max_length=280)
    created=models.DateTimeField(auto_now_add=True)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.author.username
