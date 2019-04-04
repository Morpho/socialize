from rest_framework import serializers

from ..models import Answer


class AnswerSerializer(serializers.ModelSerializer):
    """
    Serializer for Answer model. This class is directly used as
    a nested serializer inside `QuestionSerializer`.
    """
    class Meta:
        model = Answer
        exclude = ('question', 'created_at', 'updated_at', 'rank',)
