from django.db import models

from .answer import Answer
from .base import BaseModel
from .question import Question
from .quiz_details import QuizDetails


class QuizResults(BaseModel):
    """
    QuizResult model to store user reponse against each question.
    """
    quiz_details = models.ForeignKey(
        QuizDetails, on_delete=models.CASCADE, related_name='quiz_result')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
