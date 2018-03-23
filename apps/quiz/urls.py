from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from apps.quiz import views


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'quiz', views.QuizViewSet)
router.register(r'question', views.QuestionViewSet)
router.register(r'objectives', views.ObjectiveViewSet)
router.register(r'results', views.PlayViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'play/(?P<quiz>[0-9])/', views.SafeQuestionView.as_view(),
        name='safe_questions')
]

