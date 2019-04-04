from rest_framework import viewsets

from ..models import Question
from ..serializers import QuestionSerializer


class QuestionViewSet(viewsets.ModelViewSet):
    """
    Question view functions. This class supports two
    style GET endpoints.
     - /question/ ==> Get list of questions from question bank.
     - /quiz/1/question/ ==> Get list of questions associated with quiz with id 1

    The response will be according to `QuestionSerializer` class.
    """
    serializer_class = QuestionSerializer
    http_method_names = ('get',)

    def get_queryset(self):
        """
        Overidden method to support both endpoints.
        """
        queryset = Question.objects.all()
        if self.kwargs.get('quiz_pk'):
            queryset = Question.objects.filter(quiz__id=self.kwargs['quiz_pk'])
        return queryset
