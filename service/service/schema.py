# Lesson_10

'''
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


class ToDoType(DjangoObjectType):
    class Meta:
        model = TodoNote
        fields = '__all__'


class Query(graphene.ObjectType):
    # Пример
    # hello = graphene.String(default_value="Hi!")
    # ready = graphene.String(default_value="Yes!")

    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    all_todo = graphene.List(ToDoType)

    project_by_id = graphene.Field(ProjectType, id=graphene.String(required=True))

    # Фильтрация с параметрами
    def resolve_project_by_id(self, info, id):
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return TodoNote.objects.all()

    def resolve_all_users(root, info):
        return TodoUser.objects.all()


# schema = graphene.Schema(query=Query)


class ProjectMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, id):
        project = Project.objects.get(pk=id)
        project.name = name
        project.save()
        return ProjectMutation(project=project)


class Mutation(graphene.ObjectType):
    update_project = ProjectMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
'''

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
 
# Фильтрация
Запрос
{
	projectById(id: "737eddde-e197-4e2f-8f6d-f9367875d6d6") {
	name
	id
	}
}

Ответ

{
  "data": {
    "projectById": {
      "name": "New",
      "id": "737eddde-e197-4e2f-8f6d-f9367875d6d6"
    }
  }
}

# Обновление данных. В полнятиях графа Mutation

Запрос:

mutation updateProject {
	updateProject(name: "Mutation", id: "737eddde-e197-4e2f-8f6d-f9367875d6d6") {
		project {
		id
		name
		}
	}
}

Ответ:

{
  "data": {
    "updateProject": {
      "project": {
        "id": "737eddde-e197-4e2f-8f6d-f9367875d6d6",
        "name": "Mutation"
      }
    }
  }
}

# Немного о микросервисах. На Ютубе
Григорий Петров. Общение микросервисов: REST, JSON, GraphQL


'''
