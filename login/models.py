from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Account(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phoneno=models.IntegerField()
    image=models.ImageField(upload_to="accounts", blank=True, null=True )

    def save(self,*args, **kwargs):
        self.phoneno=9999999999
        super().save(*args, **kwargs)

    def __str__(self):
        return (self.user.username)