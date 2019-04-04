from django.db import models

from .base import BaseModel
from .question import Question


class Answer(BaseModel):
    """
    Answer model definition. One question can have multiple answers.
    """
    rank = models.IntegerField(help_text="Sorting order field for answers")
    text = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='question_answers')

    class Meta:
        ordering = ('rank',)
