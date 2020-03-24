from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

User = get_user_model()


# Create your models here.
class Chat(models.Model):
    content = models.CharField(max_length=50, default=None)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, related_name='author_messages')
    room = models.CharField(max_length=15, default=None)
    #password = models.CharField(max_length=20, default=None)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages():
        return Chat.objects.order_by('-timestamp').all()[:10]


'''class Room(models.Model):
    room = models.CharField(max_length=20)'''
