from django.contrib import admin
from .models import Post

# Register your models here.


class Posts(admin.ModelAdmin):
    list_display = ['id', 'profile', 'image', 'title',
                    'latitude', 'longitude', 'created_at', 'updated_at']
    list_display_link = ['id', 'profile', 'title']
    search_fields = ['profile', ]


admin.site.register(Post, Posts)
# admin.site.register(Person, Persons)
