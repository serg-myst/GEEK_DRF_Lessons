import json
from uuid import uuid4
from django.core.management.base import BaseCommand
from authapp.models import TodoUser


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:
        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('authapp/fixtures/todo_users.json')

        TodoUser.objects.all().delete()  # Почистим таблицу и загрузим новые данные
        for user in users:
            curr_user = user.get('fields')
            curr_user['id'] = uuid4()
            new_user = TodoUser(**curr_user)
            new_user.save()
