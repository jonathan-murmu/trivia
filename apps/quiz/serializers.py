from django.contrib.auth.models import User
from rest_framework import serializers
from apps.quiz.models import Objective, Question, Quiz, PlayQuiz


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('id', 'url', 'quiz_name', 'completion_time', 'scheduled_on',)


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    # objectives = serializers.RelatedField(many=True, read_only=True)

    class Meta:
        model = Question
        depth = 1
        fields = ('id', 'url', 'quiz', 'question_text', 'is_subjective',
                  'objectives')


class ObjectiveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objective
        fields = ('id', 'url', 'question', 'objective_text', 'is_answer',)


class SafeObjectiveSerializer(serializers.ModelSerializer):
    """Objective with the answer."""
    class Meta:
        model = Objective
        fields = ('id', 'url', 'question', 'objective_text',)


class SafeQuestionSerializer(serializers.HyperlinkedModelSerializer):
    """Question with choices for a particular quiz."""
    objectives = SafeObjectiveSerializer(many=True)

    class Meta:
        model = Question
        depth = 1
        fields = ('id', 'url', 'question_text', 'is_subjective',
                  'objectives')


class PlayQuizSerializer(serializers.ModelSerializer):
    """Playing the quiz."""

    class Meta:
        model = PlayQuiz
        # depth = 1
        fields = '__all__'
