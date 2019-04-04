from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from django.conf.urls import url
from django.urls import include
from .views import QuestionViewSet, QuizViewSet

router = routers.DefaultRouter()
router.register(r'quiz', QuizViewSet)
router.register(r'question', QuestionViewSet, base_name='Question')

# Nested Router for /quiz/<pk>/questions/ endpoint.
question_router = nested_routers.NestedSimpleRouter(router, r'quiz', lookup='quiz')
question_router.register(r'questions', QuestionViewSet, base_name='quiz-questions')

urlpatterns = [
  url(r'/', include(router.urls)),
  url(r'/', include(question_router.urls)),
]
