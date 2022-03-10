from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import AuthappModelSerializer

# Lesson_4
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


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

    def get(self, request, pk=None, format=None):
        todo_users = TodoUser.objects.all()
        serializer = AuthappModelSerializer(todo_users, context={'request': request}, many=True)
        return Response(serializer.data)
