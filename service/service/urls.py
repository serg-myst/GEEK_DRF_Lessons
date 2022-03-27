"""service URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter  # Lesson_1
from rest_framework.routers import DefaultRouter  # Lesson_1
from authapp.views import TodoModelViewSet  # Lesson_1
from todonotes.views import ProjectModelViewSet, TodoNoteModelViewSet  # Lesson_3
from authapp import views
from todonotes.views import ProjectAPIViewList, ProjectAPIViewDetail, ProjectAPIViewDelete, \
    ProjectAPIViewUpdate, ProjectAPIViewCreate, TodoNoteAPIViewSet # Lesson_4

# Lesson_6
from rest_framework.authtoken import views as token_views

router = DefaultRouter()
router.register('todo', TodoModelViewSet)
router.register('todoprojects', ProjectModelViewSet)
router.register('todonotes', TodoNoteModelViewSet)
router.register('todonotes-api', TodoNoteAPIViewSet, basename='todonotes_api')

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Lesson_1 в дальнейшем будем использовать
    path('api/', include(router.urls)),  # Lesson_1

    path('views/api-todo-users/', views.TodoUsersAPIVIew.as_view()),  # Lesson_4  Пример работы с APIView
    path('views/api-todo-users/<str:pk>/', views.TodoUsersAPIVIewDetail.as_view()),  # Lesson_4  Пример работы с APIView
    path('generic/api-projects/list/', ProjectAPIViewList.as_view()),  # Lesson_4  Generic Views
    path('generic/api-projects/list/<str:pk>/', ProjectAPIViewDetail.as_view()),  # Lesson_4  Generic Views
    path('generic/api-projects/delete/<str:pk>/', ProjectAPIViewDelete.as_view()),  # Lesson_4  Generic Views
    path('generic/api-projects/update/<str:pk>/', ProjectAPIViewUpdate.as_view()),  # Lesson_4  Generic Views
    path('generic/api-projects/create/', ProjectAPIViewCreate.as_view()),  # Lesson_4  Generic Views

    # Lesson_4 для фильтрации через kwargs. /<str:name>/ Придет как словарь и выкусим параметр запроса
    path('generic/api-projects/list/<str:name>/', ProjectAPIViewList.as_view()),

    # Lesson_6 url для получения токена
    path('api-token-auth/', token_views.obtain_auth_token)
]