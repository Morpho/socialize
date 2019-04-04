from rest_framework import viewsets

from ..models import Quiz
from ..serializers import QuizSerializer


class QuizViewSet(viewsets.ModelViewSet):
    """
    Viewset definition for Quiz. Supports following GET endpoint.
     - /quiz/<pk>
    """
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()
    http_method_names = ('get',)
