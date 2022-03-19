from django_filters import rest_framework as filters
from .models import Project, TodoNote

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class TodoNoteFilter(filters.FilterSet):
    create_timestamp__gt = filters.DateTimeFilter(field_name='create_timestamp', lookup_expr='gt')
    create_timestamp__lt = filters.DateTimeFilter(field_name='create_timestamp', lookup_expr='lt')

    class Meta:
        model = TodoNote
        fields = ['create_timestamp']