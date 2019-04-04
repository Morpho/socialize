from rest_framework import serializers

from ..models import Quiz

class QuizSerializer(serializers.ModelSerializer):
  """
  Serializer for Quiz model. This serializer is only one level
  deep and won't nest questions along.
  """
  class Meta:
      model = Quiz
      exclude = ('questions',)

  total_questions = serializers.IntegerField(read_only=True)
