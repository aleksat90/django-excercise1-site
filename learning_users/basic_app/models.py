from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):

    #Create releationship
    user = models.OneToOneField(User) #da bi nasledio sve USERe iz user baze


    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True) #blank true znaci da moze da ostane prazno


    def __str__(self):
        return self.user.username #default verzija User iz linije #2
