from django.db import models
from django.contrib.auth import get_user_model
from product.models import products

User = get_user_model()
# Create your models here.
class  searched(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null =True)     
    search_name = models.CharField(max_length=300)    
    date_added = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.search_name
    
class  browsed(models.Model):
    product = models.ForeignKey(products, on_delete= models.CASCADE, null=True)
    user = models.ForeignKey (User, on_delete=models.CASCADE, null =True)
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.name