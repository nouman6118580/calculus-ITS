from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('login', views.login),
    path('sign-up', views.signUp),
    path('about', views.about),
    path('quiz', views.quiz),
    path('start-quiz', views.startQuiz),
    path('calculator', views.calculator),
    path('dashboard', views.dashboard),
    path('courses', views.courses),
    path('course-content', views.courseContent),
]