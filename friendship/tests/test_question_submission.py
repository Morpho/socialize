import json
from django import test
from django.urls import reverse
from rest_framework.test import APIClient
from ..models import Question, Answer, Quiz


class TestQuestionSubmission(test.TestCase):
    """
    Class for testing Application view functions.
    """
    def setUp(self):
        """
        This method is used to create test case specific objects
        """
        self.client = APIClient()
        self.question = Question.objects.create(text='What is your name?')
        self.a1 = Answer.objects.create(rank=1, text='John Doe', question=self.question)
        self.a2 = Answer.objects.create(rank=2, text='John Doe 2', question=self.question)

    def test_new_user_submission(self):
        """
        Test submission made by new user
        """
        data = {
            "user": {"username": "johndoe"},
            "quiz": {"title": "What is your name?"},
            "quiz_result": [
                {
                    "question": self.question.id,
                    "answer": self.a1.id
                }
            ]
        }
        response = self.client.post(reverse('quizdetails-list'), data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_friend_submission(self):
        """
        Test submission made by invitation.
        """
        data = {
            "user": {"username": "johndoe"},
            "quiz": {"title": "What is your name?"},
            "quiz_result": [
                {
                    "question": self.question.id,
                    "answer": self.a1.id
                }
            ]
        }
        response = self.client.post(reverse('quizdetails-list'), data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = json.loads(response.content)
        data = {
            "user": {"username": "johndoe"},
            "invited_by": response['user']['id'],
            "quiz_result": [
                {
                    "question": self.question.id,
                    "answer": self.a1.id
                }
            ]
        }

        response = self.client.post(reverse('quizdetails-list'), data=json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 201)

        response = json.loads(response.content)
        self.assertIn('100%', response['message'])


