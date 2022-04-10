# Lesson_9
from django.urls import path
from .views import TodoUsersListApiViewGeneric

app_name = 'authapp'
urlpatterns = [
    path('', TodoUsersListApiViewGeneric.as_view()),
]
