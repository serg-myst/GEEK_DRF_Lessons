# Lesson_10

import graphene
from graphene_django import DjangoObjectType
from todonotes.models import Project, TodoNote
from authapp.models import TodoUser


class UserType(DjangoObjectType):
    class Meta:
        model = TodoUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class Query(graphene.ObjectType):
    # Пример
    # hello = graphene.String(default_value="Hi!")
    # ready = graphene.String(default_value="Yes!")

    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return TodoUser.objects.all()


schema = graphene.Schema(query=Query)


'''
Пример запроса
{
allProjects{
    id
    name
}

# Для получение еще раз того же набора данных можно использовать Alias
newProjects: allProjects{
    id
    name
}
}

# В связанных полях указываем нужные поля. В методичке просто поле (в нашем случае users), но так не работает!

{
  allProjects {
    id
    name
    users{
      id
    }
  }
}
 


'''
