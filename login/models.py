from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phoneno=models.CharField(max_length=10,default='9999999999')
    image=models.ImageField(upload_to="accounts", blank=True, null=True )

    def __str__(self):
        return (self.user.username)