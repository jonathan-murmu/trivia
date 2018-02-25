from django.contrib.auth.models import User
from django.shortcuts import render

from rest_framework import permissions, viewsets, generics
from apps.quiz.models import Quiz, Question, Objective
from apps.quiz.serializers import QuizSerializer, \
    QuestionSerializer, ObjectiveSerializer, PlaySerializer
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

class PlayView(generics.ListAPIView):
    """Play the quiz.

    get method: display the questions and objective of the quiz."""
    serializer_class = PlaySerializer

    def get(self, request, *args, **kwargs):
       return self.list(request, *args, **kwargs)

    def get_queryset(self):
        quiz = self.kwargs['quiz']
        return Question.objects.filter(quiz__pk=quiz)