from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64, null = False)
    userName = models.CharField(max_length=64, null = False)
    password = models.CharField(max_length=64, null = False)
    phoneNumber = models.CharField(max_length=64, null = True, blank=True)
    profileImage = models.CharField(max_length=255,null = True, blank=True)
    
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    followers = models.IntegerField(null = False, default=0)
    following = models.IntegerField(null = False, default=0)
    
    createdAt = models.DateField(auto_now_add=True) 
    updatedAt = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    image = models.CharField(max_length=255, null=True)
    #comments
    #reactions
    likes = models.IntegerField(default=0)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    createdAt = models.DateField(auto_now_add=True) 
    updatedAt = models.DateField(auto_now_add=True) 

#abbeyroad0277
#class Reactions