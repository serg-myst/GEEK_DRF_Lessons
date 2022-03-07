from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import TodoUser
from .serializers import AuthappModelSerializer


# Create your views here.
def index(request):
    context = {
        'path': request.get_host(),
    }
    return render(request, 'authapp/index.html', context)


class TodoModelViewSet(ModelViewSet):
    queryset = TodoUser.objects.all()
    serializer_class = AuthappModelSerializer
