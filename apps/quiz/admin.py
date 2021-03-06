from django.contrib import admin

from apps.quiz.models import Quiz, Question, Objective, PlayQuiz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'is_subjective', 'get_objective')

    def get_objective(self, obj):
        return [i['objective_text'] for i in obj.objectives.values('objective_text')]
    get_objective.short_description = 'Objectives'
    get_objective.admin_order_field = 'questions__objective_text'


class ObjectiveAdmin(admin.ModelAdmin):
    list_display = ('objective_text', 'is_answer', 'get_question',
                    'get_quiz')

    def get_question(self, obj):
        return obj.question.question_text

    def get_quiz(self, obj):
        return [i['quiz_name'] for i in obj.question.quiz.values('quiz_name')]

    get_question.short_description = 'Questions'
    get_question.admin_order_field = 'question__question_text'
    get_quiz.short_description = 'Quiz'
    get_quiz.admin_order_field = 'quiz__quiz_name'


class PlayQuizAdmin(admin.ModelAdmin):
    list_display = ('get_user', 'get_quiz', 'get_question', 'get_user_answer',
                    'is_correct')
    def get_user(self, obj):
        return obj.user.username

    def get_quiz(self, obj):
        return obj.quiz.quiz_name

    def get_question(self, obj):
        return obj.question.question_text

    def get_user_answer(self, obj):
        return obj.user_answer.objective_text

    get_question.short_description = 'Question'
    get_question.admin_order_field = 'question__question_text'
    get_quiz.short_description = 'Quiz'
    get_quiz.admin_order_field = 'quiz__quiz_name'
    get_user_answer.short_description = 'User\'s Answer'
    get_user.admin_order_field = 'user_answer__objective_text'
    get_user.short_description = 'Username'
    get_user.admin_order_field = 'user__username'

admin.site.register(Quiz)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Objective, ObjectiveAdmin)
admin.site.register(PlayQuiz, PlayQuizAdmin)
