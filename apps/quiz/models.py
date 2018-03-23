from django.db import models

from trivia.config.base import AUTH_USER_MODEL


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
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='objectives')
    objective_text = models.CharField(max_length=255)
    is_answer = models.BooleanField(default=False)

    def __str__(self):
        return self.objective_text


class PlayQuiz(models.Model):
    """Data to hold the quiz data."""
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.SET_NULL,
                             null=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.SET_NULL,
                             null=True)
    question = models.ForeignKey(Question, on_delete=models.SET_NULL,
                                 null=True)
    user_answer = models.ForeignKey(Objective, on_delete=models.SET_NULL,
                                    null=True)
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """the is correct field"""
        if self.user_answer:
            self.is_correct = self.user_answer.is_answer
        super(PlayQuiz, self).save(*args, **kwargs)