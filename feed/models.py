from platform import mac_ver
from random import choices
from django.db import models
from account.models import Person


class Post(models.Model):
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)

    POST_IMAGES = (
        ('Cats', 'https://images.pexels.com/photos/45170/kittens-cat-cat-puppy-rush-45170.jpeg'),
        ('Elephants', 'https://images.pexels.com/photos/66898/elephant-cub-tsavo-kenya-66898.jpeg'),
        ('Lion', 'https://images.pexels.com/photos/247502/pexels-photo-247502.jpeg'),
    )

    image = models.CharField(max_length=255, null=True,
                             blank=True, choices=POST_IMAGES)
    title = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# abbeyroad0277
# class Reactions
