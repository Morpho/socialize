from rest_framework import serializers

from ..models import QuizResults


class QuizResultSerializer(serializers.ModelSerializer):
    """
    Serializer for QuizResult model.
    """
    class Meta:
        model = QuizResults
        exclude = ('quiz_details',)
