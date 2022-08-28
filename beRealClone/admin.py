from django.contrib import admin
from beRealClone.models import *

# Register your models here.
class Users(admin.ModelAdmin):
    list_display = ['id', 'name', 'userName', 'phoneNumber', 'profileImage', 'latitude', 'longitude', 'followers', 'following', 'createdAt', 'updatedAt']
    list_display_link = ['id', 'name']
    search_fields =  ['name',]
    
class Posts(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'likes',  'latitude', 'longitude', 'createdAt', 'updatedAt']
    list_display_link = ['id', 'name']
    search_fields =  ['user',]
    
admin.site.register(User, Users)
admin.site.register(Post, Posts)  