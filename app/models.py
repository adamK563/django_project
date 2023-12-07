# app/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255)
    
class FormData(models.Model):
    question = models.CharField(max_length=100)
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100, blank=True, null=True, default=None)
    answer4 = models.CharField(max_length=100, blank=True, null=True, default=None)
    answer5 = models.CharField(max_length=100, blank=True, null=True, default=None)
    selected_answer = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.question