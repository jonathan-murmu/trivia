"""trivia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework.schemas import get_schema_view

schema_view = get_schema_view(title='Quiz API')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'$^', RedirectView.as_view(url='api/quiz-app')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^schema/$', schema_view),

    url(r'^api/', include('apps.authentication.urls',
                          namespace='authentication',
                          )),
    url(r'^api/quiz-app/', include('apps.quiz.urls'), name='quiz-api'),
]
