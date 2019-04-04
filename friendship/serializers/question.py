from rest_framework import serializers
from .answer import AnswerSerializer
from ..models import Question

class QuestionSerializer(serializers.ModelSerializer):
  """
  Question model serializer. It will include answer choice in response too
  through nested serializer `AnswerSerializer`
  """
  class Meta:
    model = Question
    fields = '__all__'
    depth = 1

  answers = AnswerSerializer(many=True, source='question_answers')
