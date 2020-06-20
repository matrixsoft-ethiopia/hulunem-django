from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()

# Create your models here.

class city(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self):
        return self.name

class  shops(models.Model):  
    owner = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    enterprise_type =  models.CharField(max_length=100, blank = False, null = True, default = 'ፋብሪካ')
    name = models.CharField(max_length=300, blank = False)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text', null=True)
    location1 = models.CharField(max_length=100, blank = False, null = True)
    location2 = models.CharField(max_length=100, blank = False, null = True)
    location3 = models.CharField(max_length=100, blank = False, null = True, default = 'ባህር ዳር')
    phone_number = models.CharField(max_length=20, blank = False, null = True)
    TIN_number = models.CharField(max_length=30, blank = False)
    mainimage = models.ImageField(upload_to='gallery/TIN', blank=True)
    approved = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

