from django.urls import path
from .views import *

urlpatterns = [
    path('users/',usersData, name="Users"),
    path('users/<int:id>',updateUser, name="Users"),
    path('friends/',FrndData, name="Users"),
    path('friends/<int:f_id>',removefrnd, name="Users"),


]