from django.db import models


class Quiz(models.Model):
    """Model for storing quiz."""
    quiz_name = models.CharField(max_length=255)
    completion_time = models.TimeField(null=True, blank=True)
    scheduled_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.quiz_name


class Question(models.Model):
    """Questions belonging to a quiz."""
    quiz = models.ManyToManyField(Quiz)
    question_text = models.TextField()
    is_subjective = models.BooleanField(default=False)

    def __str__(self):
        return self.question_text


class Objective(models.Model):
    """Objectives/Choices for a question."""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    objective_text = models.CharField(max_length=255)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.objective_text