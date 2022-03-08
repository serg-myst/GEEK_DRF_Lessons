from django.shortcuts import render
from rest_framework.renderers import AdminRenderer  # Lesson_3 Для собственного вывода
from rest_framework.viewsets import ModelViewSet  # Lesson_3
from .serializers import ProjectSerializer, TodoNoteSerializer  # Lesson_3
from .models import Project, TodoNote  # Lesson_3

# from djangorestframework_camel_case.renderer import CamelCaseJSONRenderer
from djangorestframework_camel_case.parser import CamelCaseJSONParser


# Create your views here.
# Lesson_3

class NoUnderscoreBeforeNumberCamelCaseJSONParser(CamelCaseJSONParser):
    json_underscoreize = {'no_underscore_before_number': True}


class ProjectModelViewSet(ModelViewSet):
    # renderer_classes = [AdminRenderer]  # Lesson_3 Вывод на экран через собственную админку (встроенная)
    # renderer_classes = [CamelCaseJSONRenderer]  # Lesson_3 Вывод на экран через собственную админку (встроенная)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # parser_classes = (NoUnderscoreBeforeNumberCamelCaseJSONParser,)  # Lesson_3


class TodoNoteModelViewSet(ModelViewSet):
    queryset = TodoNote.objects.all()
    serializer_class = TodoNoteSerializer
