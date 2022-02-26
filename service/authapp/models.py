from django.db import models
from uuid import uuid4  # Lesson_1 библиотека для работы с уидами 36 символов код генерит система
from django.contrib.auth.models import AbstractUser  # Lesson_1 Наследуемся от класса User


class TodoUser(AbstractUser):
    id = None
    # Основные поля таблицы: username, firstname, lastname, email (должен быть уникальным в пределах таблицы)
    id = models.UUIDField(primary_key=True,
                          default=uuid4)  # Первичный ключ УИД правильно использовать в качестве ключа
    email = models.EmailField(unique=True, null=False, blank=False)  # unique=True делает поле уникальным в таблицу
    birthday_year = models.PositiveIntegerField(verbose_name='Год рождения', null=True)

    def __str__(self):
        return f'{self.username} | {self.email}'
