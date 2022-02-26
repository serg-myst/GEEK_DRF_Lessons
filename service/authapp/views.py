from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import AuthappModelSerializer


# Create your views here.
class TodoModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = AuthappModelSerializer
