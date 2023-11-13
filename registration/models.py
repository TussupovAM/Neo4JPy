import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from neomodel import StructuredNode, StringProperty
from .neomodels import NeoUser

class User(AbstractUser, StructuredNode):
    email = models.EmailField(unique=True)
    neo_id = StringProperty(default=str(uuid.uuid4()), unique_index=True)

    def save(self, *args, **kwargs):
        neo_user = NeoUser(username=self.username, email=self.email)
        neo_user.save()
        super().save(*args, **kwargs)
