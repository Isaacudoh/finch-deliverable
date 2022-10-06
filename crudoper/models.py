from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Bird(models.Model):
    owner        = models.ForeignKey(User,on_delete=models.CASCADE)
    bird_breed             = models.CharField(max_length=20)
    bird_name           = models.CharField(max_length=100)
    
    def __str__(self):
        return self.bird_name

class BirdFamily(models.Model):
    name             = models.CharField(max_length=100)
    birds        = models.ManyToManyField("Bird")

    
    def __str__(self):
        return self.name

