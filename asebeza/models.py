from django.conf import settings
from django.db import models
from shop.models import shops
from django.contrib.auth import get_user_model

User = get_user_model()

# Product Model

class category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class asebeza(models.Model):
    shop = models.ForeignKey(shops, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=300)
    category =  models.ForeignKey(category, on_delete=models.SET_NULL, null=True)
    detail_text = models.TextField(max_length=1000, verbose_name='Detail Text', null=True)
    price = models.FloatField()
    stock_qty = models.FloatField(default=0)
    mainimage = models.ImageField(upload_to='gallery/asebeza', default='default.jpg', null=True, blank=True)
    date_added = models.DateTimeField(auto_now=True)
    

    def no_of_ratings(self):
        ratings = rating.objects.filter(products = self)
        return len(ratings)

    def avg_rating(self):
        sum=0
        ratings = rating.objects.filter(products = self)
        for rating2 in ratings:
            sum += rating2.star
        if len(ratings) > 0:
            return sum/len(ratings)
        else:               
            return 0
    
    def five_star(self):
        ratings = rating.objects.filter(products = self)
        ratings2 = rating.objects.filter(products = self, star = 5)
        if len(ratings)>0:
            return round(len(ratings2)/len(ratings)*100,2)
        else:
            return 0

    def four_star(self):
        ratings = rating.objects.filter(products = self)
        ratings2 = rating.objects.filter(products = self, star = 4)
        if len(ratings)>0:
            return round(len(ratings2)/len(ratings)*100,2)
        else:
            return 0

    def three_star(self):
        ratings = rating.objects.filter(products = self)
        ratings2 = rating.objects.filter(products = self, star = 3)
        if len(ratings)>0:
            return round(len(ratings2)/len(ratings)*100,2)
        else:
            return 0

    def two_star(self):
        ratings = rating.objects.filter(products = self)
        ratings2 = rating.objects.filter(products = self, star = 2)
        if len(ratings)>0:
            return round(len(ratings2)/len(ratings)*100,2)
        else:
            return 0

    def one_star(self):
        ratings = rating.objects.filter(products = self)
        ratings2 = rating.objects.filter(products = self, star = 1)
        if len(ratings)>0:
            return round(len(ratings2)/len(ratings)*100,2)
        else:
            return 0
   
    def __str__(self):
        return self.name

class asebeza_rating(models.Model):
    asebeza = models.ForeignKey(asebeza, on_delete= models.CASCADE, null=True)
    user = models.ForeignKey(User,  on_delete= models.SET_NULL, null=True)   
    star = models.IntegerField(null=True)
    
    def __str__(self):
        return self.asebeza.name



