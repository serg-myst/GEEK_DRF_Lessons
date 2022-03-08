from rest_framework.relations import StringRelatedField, PrimaryKeyRelatedField, HyperlinkedRelatedField  # Lesson_3
# PrimaryKeyRelatedField - используется по умолчанию. HyperlinkedRelatedField - так же используется
from rest_framework.serializers import HyperlinkedModelSerializer
from todonotes.models import Project, TodoNote  # Lesson_3
from authapp.serializers import AuthappModelSerializer


class ProjectSerializer(HyperlinkedModelSerializer):
    users = AuthappModelSerializer(many=True)  # Lesson_3 Важно для полей ManyToManyField. Выводи все значения

    # users = StringRelatedField(many=True)  # Lesson_3 Выводит представление пользователя. То, что прописано в __str__

    class Meta:
        model = Project
        fields = '__all__'
        # exclude = ['id',] Выводим все кроме полей, указанных в списке


class TodoNoteSerializer(HyperlinkedModelSerializer):
    user = AuthappModelSerializer()  # Lesson_3 Разворачиваем по пользовталем
    project = ProjectSerializer()  # Lesson_3 Разворачиваем по проектам

    class Meta:
        model = TodoNote
        fields = '__all__'
