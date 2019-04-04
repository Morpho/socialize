from django.db import models
from .base import BaseModel
from .quiz import Quiz

class User(BaseModel):
  """
  User model definition. A user can participate in multiple quiz and each quiz
  can be attempted by multiple users. This relationship is configured through
  `models.QuizDetails` model.

  TODO: Add fields to support facebook login.
  """
  username = models.CharField(max_length=50, unique=True)
  quiz = models.ManyToManyField(Quiz, through='QuizDetails', through_fields=('user', 'quiz'))
