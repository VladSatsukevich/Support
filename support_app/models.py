from django.db import models
from django.utils import timezone

class Room(models.Model):
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.CharField(max_length=255)
    room = models.CharField(max_length=255)
    value = models.TextField(max_length=255)
    date = models.DateTimeField(default=timezone.now, blank=True)
    answered = models.BooleanField(default=False)
    closed = models.BooleanField(default=False)
    freeze = models.BooleanField(default=False)

    class Meta:
        verbose_name: "Вопрос"
        verbose_name_plural: "Вопросы"
