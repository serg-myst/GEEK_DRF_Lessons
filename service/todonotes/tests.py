from django.test import TestCase

# Lesson 8
import json
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
from django.contrib.auth.models import User

from .views import ProjectModelViewSet, TodoNoteModelViewSet
from authapp.views import TodoUsersAPIVIew, TodoUsersAPIVIewDetail
from .models import Project, TodoNote, TodoUser


# Create your tests here.

class TestProjectViewSet(TestCase):
    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todoprojects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Тест APIClient()
    def test_get_detail(self):
        project = Project.objects.create(name='TEST', href='http://127.0.0.1:8000/views/api-todo-users/',
                                         description='TEST')
        client = APIClient()
        response = client.get(f'/generic/api-projects/list/{project.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_detail(self):
        project = Project.objects.create(name='TEST', href='http://127.0.0.1:8000/views/api-todo-users/',
                                         description='TEST')
        client = APIClient()
        response = client.put(f'/generic/api-projects/update/{project.id}/',
                              {'name': 'TEST1', 'href': 'http://127.0.0.1:8000/views/api-todo-users-test1/',
                               'description': 'TEST1'}, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_401_UNAUTHORIZED)  # неавторизованные пользователи не могут менять данные

    # Для авторизованных пользователей
    def test_edit_detail_authorized(self):
        project = Project.objects.create(name='TEST', href='http://127.0.0.1:8000/views/api-todo-users/',
                                         description='TEST')
        client = APIClient()
        admin = TodoUser.objects.create_superuser('admin', 'admin@admin.com',
                                                  'admin')
        client.login(username='admin', password='admin')
        response = client.put(f'/generic/api-projects/update/{project.id}/',
                              {'name': 'TEST1', 'href': f'http://127.0.0.1:8000/views/api-todo-users-test1/',
                               'description': 'TEST1'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.name, 'TEST1')
        self.assertEqual(project.description, 'TEST1')
        client.logout()


# Тест POST запроса
class TestTodoUsersAPIVIew(TestCase):

    def test_create_user(self):
        factory = APIRequestFactory()
        request = factory.post('/views/api-todo-users/', {'username': 'TEST', 'first_name': 'TEST', 'last_name': 'TEST',
                                                          'email': 'test@gmail.com'}, format='json')
        # Для авторизованного пользователя
        admin = TodoUser.objects.create_superuser('admin', 'admin@admin.com',
                                                  'admin123456')
        force_authenticate(request, admin)
        view = TodoUsersAPIVIew.as_view()  # Когда передаю {'post': 'create'} выдает ошибку, что много аргументов.
        # Может это из-за отдельно прописанного метода post в классе!?
        # Наследование от класса APIView
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# ТЕСТ APISimpleTestCase. Для проверки каких-то отдельных методов. Не использует базу данных
# Пример не связанный с нишим API
class TestMath(APISimpleTestCase):

    def test_sqrt(self):
        import math
        self.assertEqual(math.sqrt(4), 2)


# ТЕСТ APITestCase
class TestTodoUsersAPIVIew(APITestCase):

    def test_get_list(self):
        response = self.client.get('/views/api-todo-users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_admin(self):
        test_user = TodoUser.objects.create(username='test111', birthday_year=1993, email='test1111@mail.ru')
        admin = TodoUser.objects.create_superuser('admin', 'admin@admin.com',
                                                  'admin123456')
        self.client.login(username='admin', password='admin123456')
        response = self.client.put(f'views/api-todo-users/{test_user.id}/',
                                   {'id': test_user.id, 'username': 'test333', 'birthday_year': 1996,
                                    'email': 'test333@mail.ru'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user = TodoUser.objects.get(id=test_user.id)
        self.assertEqual(user.username, 'test333')


# Тест TodoNote
class TestTodoNoteAPIVIew(TestCase):

    def setUp(self):
        self.user = TodoUser.objects.create_superuser(
            username='ron',
            password='shippers',
            email='ship@test.com'
        )

    #  Mixer. Обязательно pip install mixer
    def test_edit_mixer(self):

        # mixer создает случайные объекты в базе
        user = mixer.blend(TodoUser)
        project = mixer.blend(Project)

        data = json.dumps({
            'project': {'id': str(project.id)},
            'user': {'id': str(user.id)},
            'note_text': 'bla bla bla',
            'create_timestamp': '2017-09-20T11:52:32-98'
        })

        client = APIClient()
        client.force_authenticate(user=self.user)

        print(str(project.id), project)

        response = self.client.post('/api/todonotes-api/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Проверим
        todo = TodoNote.objects.get(note_text='bla bla bla')
        print(todo.id)
        self.assertEqual(todo.note_text, 'bla bla bla')
