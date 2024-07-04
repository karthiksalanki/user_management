from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
# class User(AbstractUser):
#     friends = models.ManyToManyField('self', through='Friend', symmetrical=False, related_name='friend_of')
#     pass

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.DO_NOTHING)
    friend = models.ManyToManyField(User, related_name='friend_of')

    class Meta:
        verbose_name = 'USER FRIEND'
        verbose_name_plural = 'USER FRIENDS'



# class User(AbstractUser):
#     friends = models.ManyToManyField('self', through='Friend', symmetrical=False, related_name='friend_of')

#     def __str__(self):
#         return self.username

# class Friend(models.Model):
#     user = models.ForeignKey(User, related_name='user_friends', on_delete=models.DO_NOTHING)
#     friend = models.ForeignKey(User, related_name='friends_with', on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         unique_together = ('user', 'friend')

    # def __str__(self):
    #     return f"{self.user.username} is friends with {self.friend.username}"