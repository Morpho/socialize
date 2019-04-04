from django import test
from django.urls import reverse
from rest_framework.test import APIClient
from ..models import Question, Answer, Quiz


class TestQuestionViewSet(test.TestCase):
    """
    Class for testing Application view functions.
    """
    def setUp(self):
        """
        This method is used to create test case specific objects
        """
        self.client = APIClient()
        question = Question.objects.create(text='What is your name?')
        Answer.objects.create(rank=1, text='John Doe', question=question)
        Answer.objects.create(rank=2, text='John Doe 2', question=question)

        self.quiz = Quiz.objects.create(title='Name Test')
        self.quiz.questions.add(question)

    def test_question_get(self):
        """
        Test question GET.
        """
        response = self.client.get(reverse('question-list'))
        self.assertEqual(response.status_code, 200)

    def test_quiz_question_get(self):
        """
        Test quiz question GET.
        """
        response = self.client.get(reverse('quiz-questions-list', kwargs={"quiz_pk": self.quiz.id}))
        self.assertEqual(response.status_code, 200)


