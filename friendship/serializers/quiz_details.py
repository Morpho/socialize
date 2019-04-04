from django.urls import reverse

from rest_framework import serializers

from ..models import Quiz, QuizDetails, QuizResults, User
from .quiz import QuizSerializer
from .quiz_results import QuizResultSerializer
from .user import UserSerializer


class QuizDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer class of QuizDetails model. This class is responsible for
    saving user responses, generating invitation links and receiving quiz
    responses from other friends.
    """
    class Meta:
        model = QuizDetails
        fields = '__all__'

    message = serializers.CharField(read_only=True)
    invitation_link = serializers.SerializerMethodField()

    quiz = QuizSerializer(required=False)
    user = UserSerializer()
    invited_by = serializers.PrimaryKeyRelatedField(
        required=False, queryset=QuizDetails.objects.all())
    quiz_result = QuizResultSerializer(many=True, write_only=True)

    def create(self, validated_data):
        """
        This method is overidden to provide support for creating m2m models.
        It will first create user then quiz followed by QuizDetails and finally
        QuizResults. It manages the special case when a user is invited by some
        other user too.
        """
        quiz_result = validated_data.get('quiz_result')
        invited_by = validated_data.get('invited_by')
        user = validated_data.get('user')
        quiz = validated_data.get('quiz')

        user, _ = User.objects.get_or_create(**user)

        # If user is not invited by someone, create new quiz.
        if not invited_by:
            quiz = Quiz.objects.create(**quiz)
            quiz.questions.set([result.get('question')
                                for result in quiz_result])
        # Otherwise the quiz already exist in the system just fetch it.
        else:
            quiz = invited_by.quiz

        quiz_details = QuizDetails.objects.create(
            user=user, quiz=quiz, invited_by=invited_by)
        QuizResults.objects.bulk_create(
            [QuizResults(**result, quiz_details=quiz_details) for result in quiz_result])

        return quiz_details

    def get_invitation_link(self, obj):
        """
        This method will provide invitation link so the quiz can
        be shared with friends.
        """
        return reverse('quizdetails-detail', kwargs={'pk': obj.id})
