from django.db import models
from .base import BaseModel
from .quiz import Quiz
from .user import User

class QuizDetails(BaseModel):
  """
  Associative entity between `Quiz` and `User`. It also has a self reference to indicated
  if a user is invited by another user. This is helpful in calculating similarity score.
  This is the main entity use when user submits a quiz or when an invitation link is clicked.

  Right now the contraints are not strict on this model. A user can take same quiz multiple times.
  A user can also invite same user multiple times and he can attempt the same quiz. This can however
  be changes based on business requirements.
  """
  invited_by = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
  quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  @property
  def message(self):
    """
    Message attribute for QuizDetails. If user is not invited by
    anyone a default message will be returned. Otherwise message
    will contains information on how many responses are similar for
    both users. Rule for custom message are as follows:

    - Score below 35%(inclusive) will says `just ok` similarity.
    - Score above 35% will say `well` similarity.
    - Score above 60%(exclusive) will say `very well` similarity.
    """
    default_message = "Thanks for taking this quiz. Share this quiz with your friends and see how they answer"
    result_message = "You know your friend {username} {score}. You answered {percent}% questions like him"
    score = 'just ok'

    if not self.invited_by:
      return default_message

    total_questions = self.quiz.total_questions
    friend_responses = self.invited_by.quiz_result.values('question', 'answer').order_by('question').all()
    user_responses = self.quiz_result.values('question', 'answer').order_by('question').all()

    # Check how many responses are similar
    matching_responses = len([
      i for i in friend_responses for j in user_responses
      if i['question']==j['question'] and i['answer']==j['answer']]
    )

    # Calculate percentage match
    percent_match = (matching_responses // total_questions) * 100

    if percent_match > 35:
      score = 'well'

    if percent_match > 60:
      score = 'very well'

    return result_message.format(username=self.invited_by.user.username, score=score, percent=percent_match)
