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
    ProjectAPIViewUpdate, ProjectAPIViewCreate, TodoNoteAPIViewSet  # Lesson_4

# Lesson_6
from rest_framework.authtoken import views as token_views

# Lesson_9
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.urls import re_path  # Lesson_9

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
# Lesson_9 end

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
    path('api-token-auth/', token_views.obtain_auth_token),

    # Lesson_9
    re_path(r'^api/(?P<version>\d\.\d)/users/$', views.TodoUsersListApiViewGeneric.as_view()),
    re_path(r'^api/apiview/(?P<version>\d\.\d)/users/$', views.TodoUsersAPIVIew.as_view()),

    path('api/users/0.1', include('authapp.urls', namespace='0.1')),
    path('api/users/0.2', include('authapp.urls', namespace='0.2')),

    # Получение версии через параметры
    path('api/users_ver/', views.TodoUsersListApiViewGeneric.as_view()),

    # Lesson_9 Документация. Обязательно pip install -U drf-yasg
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
