from django.db import models

# Create your models here.
class userslist(models.Model):
    fname = models.CharField(max_length=100)
    mname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=100)
    useremail = models.CharField(max_length=100)
    userphone = models.CharField(max_length=100)
    regdate = models.DateTimeField(auto_now_add=True)
 