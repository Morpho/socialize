from django.db import models
from .base import BaseModel
from .quiz_details import QuizDetails
from .question import Question
from .answer import Answer

class QuizResults(BaseModel):
  """
  QuizResult model to store user reponse against each question.
  """
  quiz_details = models.ForeignKey(QuizDetails, on_delete=models.CASCADE, related_name='quiz_result')
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
