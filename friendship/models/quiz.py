from django.db import models
from .base import BaseModel
from .question import Question

class Quiz(BaseModel):
  """
  Model definition for quiz class. The idea is when a user answer
  a particular set of questions a new quiz will be created that
  he can share with his friends.

  A quiz can have multiple questions and a questions can be in multiple quizes.
  """
  title = models.CharField(max_length=50)
  questions = models.ManyToManyField(Question)

  @property
  def total_questions(self):
    """
    Property definition to get total number of questions in a quiz.
    """
    return self.questions.count()
