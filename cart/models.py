from django.db import models
from product.models import products
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your models here.

class cart(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null =True)
    product = models.ForeignKey(products, on_delete= models.CASCADE, null=True)
    cart_date = models.DateField(auto_now=True)   
     
class order(models.Model):
    user = models.ForeignKey (User, on_delete=models.CASCADE, null =True)
    product = models.ForeignKey(products, on_delete= models.CASCADE, null=True)
    order_date = models.DateField(auto_now=True)
    location1 = models.CharField(max_length=100, blank = False, null = True)
    location2 = models.CharField(max_length=100, blank = False, null = True)
    location3 = models.CharField(max_length=100, blank = False, null = True, default = 'ባህር ዳር')
    phone_number = models.CharField(max_length=20, blank = False, null = True) 
     
    def __str__(self):
        return self.product.name
    