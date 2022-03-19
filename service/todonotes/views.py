from django.shortcuts import render
from rest_framework.renderers import AdminRenderer  # Lesson_3 Для собственного вывода
from rest_framework.viewsets import ModelViewSet  # Lesson_3
from .serializers import ProjectSerializer, TodoNoteSerializer  # Lesson_3
from .models import Project, TodoNote  # Lesson_3

# from djangorestframework_camel_case.renderer import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import CamelCaseJSONParser

# Lesson_4 Concrete View Classes
# https://www.django-rest-framework.org/api-guide/generic-views/
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView
from django.shortcuts import get_object_or_404
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status  # https://www.django-rest-framework.org/tutorial/3-class-based-views/
from rest_framework import viewsets  # Lesson_4

from authapp.models import TodoUser

from rest_framework.pagination import LimitOffsetPagination  # Lesson_4

from .filters import ProjectFilter, TodoNoteFilter  # Lesson_4 Работа с фильтром

from datetime import datetime


# Create your views here.
# Lesson_3

class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}


# Lesson_4 Подключаем пагинацию. Для проектов ограничение 10
class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoNoteLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer]  # Lesson_3 Вывод на экран через собственную админку (встроенная)
    # renderer_classes = [CamelCaseJSONRenderer]  # Lesson_3 Вывод на экран через собственную админку (встроенная)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    # parser_classes = (NoUnderscoreBeforeNumberCamelCaseJSONParser,)  # Lesson_3
    filterset_class = ProjectFilter


class TodoNoteModelViewSet(ModelViewSet):
    queryset = TodoNote.objects.all()
    serializer_class = TodoNoteSerializer
    pagination_class = TodoNoteLimitOffsetPagination
    filterset_class = TodoNoteFilter


# Lesson_4 Запросы к таблицу Project построим на Generic Views
# Следующий уровень APIView. Уже содержит в себе get обработчик
class ProjectAPIViewList(ListAPIView):
    # renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination

    # Используем библиотеку django-filter. В стандартном интерфейсе появится кнопка Filters
    # filterset_fields = ['name', 'description']

    # Собственные фильтры в файле filters.py В данном случае по словосочетанию в имени
    # https://django-filter.readthedocs.io/en/latest/index.html
    filterset_class = ProjectFilter

    # Это способ без использования библиотеки django-filter
    # def get_queryset(self):
    # Работа через параметры
    # return Project.objects.filter(name__contains='git') # Пример
    #    name = self.request.query_params['name'][0]
    # Приходит в виде кода из url ?name=Name&car=Ferrari
    # {'name': ['Name'], 'car': 'Ferrari'} - приходит словарь
    # Приход в виде кода из url ?name=Name&name=Ferrari
    # {'name': ['Name',Ferrari']} - приходит словарь

    # работа через Headers. Заголовки http запроса
    #    name = self.request.headers.get('name')
    # {'Content-Length': '', 'Content-type': 'text/plain', 'Name': 'Alex' и т.д.}

    # Работа через kwargs. Передаем текст фильтра в самом url.
    # Обязательно прописать в маршрутах. path('generic/api-projects/list/<str:name>/'
    #    name = self.kwargs['name']

    #    return Project.objects.filter(name__contains=name)


class ProjectAPIViewDelete(DestroyAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAPIViewUpdate(UpdateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectAPIViewCreate(CreateAPIView):
    renderer_classes = [JSONRenderer]

    # queryset = Project.objects.all()
    # serializer_class = ProjectSerializer

    # Переопределил метод. Не понимаю как в моделе сделать
    # Без этого не получается загрузить JSON
    # {
    #    "name": "Проект создали Create112453",
    #    "href": "https://github.com/serg/GEEK_DRF_Lessons/pull/3",
    #    "description": "Какое-то описание проекта. Create.",
    #    "users": [
    #        {
    #            "id": "0ea8bf17-3e77-4817-a4a5-a19f90cd7c5d"
    #        },
    #        {
    #            "id": "283d763e-413a-4a1b-84aa-824158afce6d"
    #        }
    #    ]
    # }
    def create(self, request):
        data = request.data['users']
        project = Project.objects.create(name=data['name'], href=data['href'], description=data['description'])
        for user in data:
            project.users.add(TodoUser.objects.get(id=user['id']))
        project.save()
        return Response(status=status.HTTP_201_CREATED)


# Получает конкретную позицию
# http://127.0.0.1:8000/generic/api-projects/c279871b-cb08-4cd2-96b2-780cbfd80b5d/
class ProjectAPIViewDetail(RetrieveAPIView):
    renderer_classes = [JSONRenderer]
    queryset = obj = Project.objects.all()
    serializer_class = ProjectSerializer


# Lesson_4 CRUD для TodoNote
# https://www.django-rest-framework.org/api-guide/viewsets/
class TodoNoteAPIViewSet(viewsets.ViewSet):
    # renderer_classes = [JSONRenderer]
    pagination_class = TodoNoteLimitOffsetPagination

    def get_date_from_str(self, date):
        return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')

    def list(self, request):
        # Lesson_4 Получим параметры из запроса
        # Пример строки запроса:
        # http://127.0.0.1:8000/api/todonotes-api/?create_date_gt=2022-03-16T12:31:42.857710&create_date_lt=2022-03-18T12:31:42.857710&/
        create_timestamp_gt = self.request.query_params.get('create_date_gt')
        create_timestamp_lt = self.request.query_params.get('create_date_lt')

        if create_timestamp_gt and create_timestamp_lt:
            print(self.get_date_from_str(create_timestamp_gt))
            todo_notes = TodoNote.objects.filter(create_timestamp__range=(
                self.get_date_from_str(create_timestamp_gt),
                self.get_date_from_str(create_timestamp_lt)))
        else:
            todo_notes = TodoNote.objects.all()

        serializer = TodoNoteSerializer(todo_notes, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo_note = get_object_or_404(TodoNote, pk=pk)
        serializer_class = TodoNoteSerializer(todo_note)
        return Response(serializer_class.data)

    # https://stackoverflow.com/questions/35543775/django-rest-create-object-with-foreign-key-using-serializers
    def create(self, request):
        serializer = TodoNoteSerializer(data=request.data)
        if serializer.is_valid():
            project = Project.objects.get(id=request.data['project']['id'])
            user = TodoUser.objects.get(id=request.data['user']['id'])
            serializer.save(user=user, project=project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        todo_note = get_object_or_404(TodoNote, pk=pk)
        serializer = TodoNoteSerializer(todo_note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        todo_note = get_object_or_404(TodoNote, pk=pk)
        serializer = TodoNoteSerializer(todo_note)
        if todo_note:
            todo_note.is_active = False
            todo_note.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
