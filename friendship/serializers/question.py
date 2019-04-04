from rest_framework import serializers

from ..models import Question
from .answer import AnswerSerializer


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
