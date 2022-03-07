from django.db import models
from uuid import uuid4
from authapp.models import TodoUser


# Lesson_3 Создаем модели
class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)  # Ключ
    name = models.CharField(max_length=128, unique=True)  # Название проекта. Сделаем уникальным
    href = models.URLField(verbose_name='Ссылка на репозиторий')  # Может быть ссылка на репозиторий
    description = models.TextField(verbose_name='Описание проекта')  # Описание проекта
    users = models.ManyToManyField(TodoUser)

    def __str__(self):
        return self.name


class TodoNote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)  # Ключ
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(TodoUser, on_delete=models.CASCADE)
    note_text = models.TextField(verbose_name='Текст заметки', default=False)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)


