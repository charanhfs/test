# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserManager(models.Manager):
    def check_user(self, data):
        errors = []
        if len(data['username']) < 8:
            errors.append(['username should be more than 8 characters!'])
        if len(data['username']) > 16:
            errors.append(['username should be less than 16 characters!'])
        if errors:
            return [False, errors]
        else:
            newUser = User(username = data['username'])
            newUser.save()
            return [True, newUser]



class User(models.Model):
    username = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
