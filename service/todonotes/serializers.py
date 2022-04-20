from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField, HyperlinkedRelatedField  # Lesson_3
# PrimaryKeyRelatedField - используется по умолчанию. HyperlinkedRelatedField - так же используется
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from todonotes.models import Project, TodoNote  # Lesson_3
from authapp.serializers import AuthappModelSerializer


class ProjectSerializer(ModelSerializer):
    users = AuthappModelSerializer(read_only=True ,many=True)  # Lesson_3 Важно для полей ManyToManyField. Выводит все значения.

    # read_only=True - позволяет добавить запись без пользователей. Не совсем понятно.
    # Ведь связи по пользоватлеям это отдельная таблица

    # users = StringRelatedField(many=True)  # Lesson_3 Выводит представление пользователя. То, что прописано в __str__

    class Meta:
        model = Project
        # fields = '__all__'
        fields = ('id', 'name', 'href', 'description', 'users')
        # exclude = ['id'] # Выводим все кроме полей, указанных в списке


class TodoNoteSerializer(ModelSerializer):
    user = AuthappModelSerializer(read_only=True)  # Lesson_3 Разворачиваем по пользовталем
    project = ProjectSerializer(read_only=True)  # Lesson_3 Разворачиваем по проектам

    class Meta:
        model = TodoNote
        fields = ('id', 'project', 'user', 'note_text', 'create_timestamp')
