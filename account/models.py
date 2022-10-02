from random import choices
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    bio = models.TextField(null=True, blank=True)

    phone_number = models.CharField(max_length=64, null=True, blank=True)

    PROFILE_IMAGES = (
        ('Puppy', 'https://images.pexels.com/photos/39317/chihuahua-dog-puppy-cute-39317.jpeg'),
        ('Rabbit', 'https://images.pexels.com/photos/4588065/pexels-photo-4588065.jpeg'),
    )

    profile_image = models.CharField(
        max_length=255, null=True, blank=True, choices=PROFILE_IMAGES)

    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    following = models.ManyToManyField(
        'self', symmetrical=False, related_name='followers')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def following_count(self):
        return self.following.count()

    def followers_count(self):
        return self.followers.count()


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=User)
