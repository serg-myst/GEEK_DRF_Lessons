from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet  # Lesson_3
from .serializers import ProjectSerializer, TodoNoteSerializer  # Lesson_3
from .models import Project, TodoNote  # Lesson_3


# Create your views here.
# Lesson_3
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TodoNoteModelViewSet(ModelViewSet):
    queryset = TodoNote.objects.all()
    serializer_class = TodoNoteSerializer
