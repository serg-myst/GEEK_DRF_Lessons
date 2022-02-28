from rest_framework.serializers import HyperlinkedModelSerializer
from .models import TodoUser


class AuthappModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoUser
        # fields = '__all__'  # По домашнему заданию написано выбрать не все поля.
        # Пока не понятно как переходить по отборам без ID
        fields = ('id', 'username', 'first_name', 'last_name', 'email')
