from rest_framework.serializers import HyperlinkedModelSerializer  # Lesson_3
from .models import TodoUser
from rest_framework.serializers import ModelSerializer


class AuthappModelSerializer(ModelSerializer):
    class Meta:
        model = TodoUser
        # fields = '__all__'  # По домашнему заданию написано выбрать не все поля.
        fields = ('id', 'url', 'username', 'first_name', 'last_name', 'email')
