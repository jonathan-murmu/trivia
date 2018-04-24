from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import permissions, viewsets, generics
from apps.quiz.mixins import CreateListMixin
from apps.quiz.models import Quiz, Question, Objective, PlayQuiz
from apps.quiz.serializers import QuizSerializer, \
    QuestionSerializer, ObjectiveSerializer, SafeQuestionSerializer, \
    PlayQuizSerializer
from apps.quiz.permissions import IsAdminOrReadOnly


class QuizViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class QuestionViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class ObjectiveViewSet(viewsets.ModelViewSet):
    """"""
    queryset = Objective.objects.all()
    serializer_class = ObjectiveSerializer


class SafeQuestionView(generics.ListAPIView):
    """Questions for the quiz.

    Display questions with objective, no answers.
    get method: display the questions and objective of the quiz."""
    serializer_class = SafeQuestionSerializer

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        return Question.objects.filter(quiz__pk=quiz)


class PlayViewSet(CreateListMixin, viewsets.ModelViewSet):
    """Api to play the quiz.

    post method submits the quiz answers by particular user."""
    queryset = PlayQuiz.objects.all()
    serializer_class = PlayQuizSerializer