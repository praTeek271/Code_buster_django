from django.db import models

# Create your models here.
subject_choice=((('Python', 'Python'), ('Java', 'Java'),('C++', 'C++'),('Front-End', 'Front-End'),('Back-End', 'Back-End'),('Others','Others'),))
img_choice=((('\_@Cache\doc-resourses.png',"doc_resource"),('\_@Cache\video-resourses.png',"vedio_resource"),('\_@Cache\winged-sword_38006.png','none')))

class Team(models.Model):
    name=models.CharField(max_length=200)
    user_img=models.ImageField( upload_to='team',blank=False,null=False)
    position=models.CharField(max_length=200)
    desc=models.CharField(max_length=500)
    lnkdin_url=models.URLField(max_length=500,null=True, blank=True)
    insta_url=models.URLField(max_length=500,null=True, blank=True)
    tweet_url=models.URLField(max_length=500,null=True, blank=True)
    fb_url=models.URLField(max_length=500,null=True, blank=True)

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
    name=models.CharField(max_length=100)
    subject=models.CharField(choices=subject_choice,max_length=200,default='none')
    category=models.CharField(max_length=200,default="Others")
    url=models.URLField(max_length=1000,null=True, blank=True)
    image=models.ImageField(choices=img_choice,upload_to="icon",null=True, blank=True)
    show=models.BooleanField()

    def __str__(self):
        if self.show:
            shown="yes"
        else:
            shown="no"
        return(f"{self.name}-:-{self.category}-:-{self.subject}")
    
    