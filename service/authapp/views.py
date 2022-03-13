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


# Create your views here.
def index(request):
    context = {
        'path': request.get_host(),
    }
    return render(request, 'authapp/index.html', context)


# Lesson_3
class TodoModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = AuthappModelSerializer


# Lesson_4
# Наследуемся от класса APIView Это базовый класс для Views в DRF. Он может быть связан с
# другими частями DRF (например, Renderers) и позволяет полностью самостоятельно написать код
# обработки того или иного запроса
class TodoUsersAPIVIew(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        todo_users = TodoUser.objects.all()
        serializer = AuthappModelSerializer(todo_users, context={'request': request}, many=True)
        return Response(serializer.data)

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