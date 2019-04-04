from rest_framework import viewsets

from ..models import QuizDetails
from ..serializers import QuizDetailsSerializer


class QuizDetailsViewSet(viewsets.ModelViewSet):
    """
    Viewset definition for quiz details. Support GET and POST methods.
     - GET /quiz_details/1
     - POST /quiz_details/ -d {...}
    """
    serializer_class = QuizDetailsSerializer
    queryset = QuizDetails.objects.all()
    http_method_names = ('get', 'post',)
