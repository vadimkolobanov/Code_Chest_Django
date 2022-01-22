from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.models import Project
from main.serializer import ProjectModelSerializer


class ProjectsLanguageLevelFiltersView(ListAPIView):
    '''
    Класс выполняющий фильтрацию проектов с передаваемыми параметрами в url
    Пример url: http://127.0.0.1:8000/api/projects/js/2/
    Вернет все проекты с языком программирования js и уровнем 2.
    '''
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        language = self.kwargs['language']
        level = self.kwargs['level']

        return Project.objects.filter(
            Q(programming_language__icontains=language) &
            Q(level__icontains=level) & Q(check=True)
        )
