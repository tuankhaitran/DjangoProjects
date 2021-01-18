from django.db import models

from django.contrib import auth 
# We can just inherit from this to build our own User class faster
# Meaning we take advantage of Django authorization  system they have for their users
# Create your models here.

class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)




