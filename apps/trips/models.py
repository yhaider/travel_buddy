from __future__ import unicode_literals
from django.db import models
from ..users.models import User, UserManager
from datetime import datetime
import bcrypt
import re

class TripManager(models.Manager):
    def validator(self, postData):
        errors = {}
        if len(postData['destination']) < 1:
            errors['destinationlength'] = "Destination field cannot be blank."
        if len(postData['description']) < 1:
            errors['descriptionlength'] = "Description field cannot be blank."
        if len(postData['start_date']) < 1:
            errors['startlength'] = "Date fields cannot be blank."
        elif postData['start_date'] < str(datetime.now()):
            errors['paststart'] = "Start date must be in the future."
        if len(postData['end_date']) < 1:
            errors['endlength'] = "Date fields cannot be blank."
        elif postData['end_date'] < str(datetime.now()):
            errors['pastend'] = "End date must be in the future."
        if postData['start_date'] > postData['end_date']:
            errors['dateerror'] = "Start date must be before the end date."
        return errors


class Trip(models.Model):
    destination = models.CharField(max_length = 255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    users = models.ManyToManyField(User, related_name = "trips")
    objects = TripManager()
