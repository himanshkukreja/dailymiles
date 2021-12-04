from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# 1-> male
# 0-> female

class feedbackmsg(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.IntegerField(blank=True, null=True)
    contact = models.FloatField(blank=True, null=True)
    message = models.FloatField(blank=True, null=True)
    
    def __str__(self):
        return self.user.username