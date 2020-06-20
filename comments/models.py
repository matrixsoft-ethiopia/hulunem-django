from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class  question(models.Model):  
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text', null=True)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class  comment(models.Model):  
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text', null=True)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username

class  claim(models.Model):  
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text', null=True)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username