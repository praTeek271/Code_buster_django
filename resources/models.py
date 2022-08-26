from django.db import models

# Create your models here.


class Team(models.Model):
    name=models.CharField(max_length=200)
    user_img=models.ImageField( upload_to='media/team', height_field=None, width_field=None, max_length=None)
    position=models.CharField(max_length=200)
    desc=models.CharField(max_length=50)
    lnkdin_url=models.URLField(max_length=500)
    insta_url=models.URLField(max_length=500)
    tweet_url=models.URLField(max_length=500)
    fb_url=models.URLField(max_length=500)

    def __str__(self):
        return(f'''{self.name}   --    {(self.position).upper()}''')


    

class FeedBack(models.Model):
    name=models.CharField(max_length=30,null=True, blank=True)
    email=models.EmailField(null=True, blank=True)
    subject=models.CharField(max_length=11,null=True, blank=True)
    desc=models.CharField(max_length=200,null=True, blank=True)
    date=models.DateField()

    def __str__(self):
        return(self.subject)


class FAQ(models.Model):
    que=models.CharField(max_length=800)
    ans=models.CharField(max_length=1000)


    def __str__(self):
        return (self.que)


class Resourses(models.Model):
    category=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    url=models.URLField(max_length=1000)
    show=models.BooleanField()

    def __str__(self):
        if self.show:
            shown="yes"
        else:
            shown="no"
        return("{0}--{1}----------|| shown  ( {2} )".format(self.category,self.name,shown))
    
    