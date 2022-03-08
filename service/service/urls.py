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
from authapp.views import TodoModelViewSet  # Lesson_1
from todonotes.views import ProjectModelViewSet, TodoNoteModelViewSet  # Lesson_3
from authapp import views


router = DefaultRouter()
router.register('todo', TodoModelViewSet)
router.register('todoprojects', ProjectModelViewSet)
router.register('todonotes', TodoNoteModelViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Lesson_1 в дальнейшем будем использовать
    path('api/', include(router.urls)),  # Lesson_1
]
