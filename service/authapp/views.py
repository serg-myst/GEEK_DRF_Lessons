from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import AuthappModelSerializer

# Lesson_4
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status  # https://www.django-rest-framework.org/tutorial/3-class-based-views/
from django.http import Http404  # https://www.django-rest-framework.org/tutorial/3-class-based-views/

from rest_framework.pagination import LimitOffsetPagination  # Lesson_4
from authapp.pagination import PaginationHandlerMixin

# Lesson_6. Права
# AllowAny — доступ есть у всех пользователей, включая неавторизованных
# IsAuthenticated — доступ есть только у авторизованных пользователей
# IsAdminUser — доступ есть только у администратора.
# IsAuthenticatedOrReadOnly — доступ есть у авторизованных пользователей, у
# неавторизованных — доступ только на просмотр данных
# DjangoModelPermissions — использует систему прав Django на модели. Для каждой модели у
# пользователя могут быть права add, change, delete, view
# DjangoModelPermissionsOrReadOnly — аналогично DjangoModelPermissions, но с правом на
# просмотр у пользователей, не обладающих другими правами.

from rest_framework.permissions import AllowAny


# Create your views here.
def index(request):
    context = {
        'path': request.get_host(),
    }
    return render(request, 'authapp/index.html', context)


# Lesson_4 Подключаем пагинацию
class TodoUsersLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


# Lesson_3
class TodoModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = AuthappModelSerializer
    pagination_class = TodoUsersLimitOffsetPagination  # Lesson_4


# Lesson_4
# Наследуемся от класса APIView Это базовый класс для Views в DRF. Он может быть связан с
# другими частями DRF (например, Renderers) и позволяет полностью самостоятельно написать код
# обработки того или иного запроса
# Работа с пагинацией
# https://medium.com/@fk26541598fk/django-rest-framework-apiview-implementation-pagination-mixin-c00c34da8ac2
# https://django.fun/docs/django-rest-framework/ru/3.12/api-guide/pagination/
class TodoUsersAPIVIew(APIView, PaginationHandlerMixin):
    renderer_classes = [JSONRenderer]
    pagination_class = TodoUsersLimitOffsetPagination
    serializer_class = AuthappModelSerializer
    permission_classes = [AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        todo_users = TodoUser.objects.all()
        # serializer = AuthappModelSerializer(todo_users, context={'request': request}, many=True)
        # serializer = self.serializer_class(todo_users, many=True)
        # return Response(serializer.data,status=status.HTTP_200_OK)

        # Подключаем пагинацию
        page = self.paginate_queryset(todo_users)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,
                                                                           many=True).data)
        else:
            serializer = self.serializer_class(todo_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Lesson_4 Запрос на запись данных в базу POST. Здесь для примера по ТЗ не нужен
    # def post(self, request, format=None):
    #    serializer = AuthappModelSerializer(data=request.data, context={'request': request})
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Lesson_4 Вывод по деталям
class TodoUsersAPIVIewDetail(APIView):
    renderer_classes = [JSONRenderer]

    def get_object(self, pk):
        try:
            return TodoUser.objects.get(pk=pk)
        except ValueError:
            raise Http404

    def get(self, request, pk, format=None):
        todo_user = self.get_object(pk)
        serializer = AuthappModelSerializer(todo_user, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        todo_user = self.get_object(pk)
        serializer = AuthappModelSerializer(todo_user, context={'request': request}, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Lesson_4 Для тестирования. По ТЗ этот метод не нужен.
    # Не забывать добавлять / в конце запроса
    # http://127.0.0.1:8000/views/api-todo-users/d7fef023-7efe-4ad2-81ba-2182387a2361/
    # def delete(self, request, pk, format=None):
    #    todo_user = self.get_object(pk)
    #    # todo_user.delete() # Непосредственное удаление
    #    todo_user.is_active = False
    #    todo_user.save()
    #    return Response(status=status.HTTP_204_NO_CONTENT)

# Если какого-то метода нет POSTMAN выдаст
# {
#    "detail": "Method \"DELETE\" not allowed."
# }
