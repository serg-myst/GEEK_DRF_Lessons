from django.contrib import admin
from .models import Project, TodoNote


# Register your models here.
admin.site.register(Project)
admin.site.register(TodoNote)
