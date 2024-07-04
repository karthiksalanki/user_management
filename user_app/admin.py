from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Friend)
class FriendAdmin(admin.ModelAdmin):
    list_display = ['user','display_Friends']

    def display_Friends(self, obj):
        return ', '.join([item.username for item in obj.friend.all()])

    display_Friends.short_description = 'Friends'