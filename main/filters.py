from django.db.models import Q
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from main.models import Project
from main.serializer import ProjectModelSerializer


class ProjectsLanguageLevelFiltersView(ListAPIView):
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        language = self.kwargs['language']
        level = self.kwargs['level']

        return Project.objects.filter(
            Q(programming_language__icontains=language) &
            Q(level__icontains=level)
        )
