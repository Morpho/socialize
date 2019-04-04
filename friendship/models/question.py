from django.db import models

from .base import BaseModel


class Question(BaseModel):
    """
    Question model definition.
    """
    text = models.CharField(max_length=500)
