from django.contrib import admin

from apps.quiz.models import Quiz, Question, Objective


class QuizAdmin(admin.ModelAdmin):
    pass


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question)
admin.site.register(Objective)