# Lesson_3 Работа с сериализаторами

from rest_framework import serializers
from ex import Author
from rest_framework.renderers import JSONRenderer


class AuthorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=120)
    birthday_year = serializers.IntegerField()


author = Author('Грин', 1880)
serializer = AuthorSerializer(author)
print(serializer.data)

# Преобразуем данные словаря в JSON
render = JSONRenderer()
json_data = render.render(serializer.data)

print(json_data)