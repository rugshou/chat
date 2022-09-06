from django.db import models
from django.utils import timezone
from django.urls import reverse_lazy


class Post(models.Model):
    email_address = models.TextField
    datetime = models.DateTimeField(default=timezone.now)
    user = models.TextField(default=timezone.now)

    def get_absolute_url(self):
        return reverse_lazy("top", args=[self.user])


class Name(models.Model):
    first_name1 = models.TextField
    last_name1 = models.TextField
    first_name2 = models.TextField
    last_name2 = models.TextField


class Chat(models.Model):
    user = models.TextField
    chat = models.TimeField
