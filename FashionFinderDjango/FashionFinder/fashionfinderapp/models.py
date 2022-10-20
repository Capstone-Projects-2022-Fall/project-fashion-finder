from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseModel(models.Model):
    """
    Base model from which other models inherit. 
    Provides created_at/ updated_at functionality.
    """
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        abstract = True

    def to_json(self):
        return None


class User(AbstractUser, BaseModel):
    """
    Django User model.
    """
    def to_json(self):
        d = dict(
            id=self.id,
            username=self.username,
            first_name=self.first_name,
            last_name=self.last_name
        )
        return d