from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1-> male
# 0-> female

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True)
    sex = models.IntegerField(default=1)
    isAdmin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
