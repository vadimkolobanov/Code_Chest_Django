from rest_framework.viewsets import ModelViewSet

from .filters import ProjectsLanguageLevelFiltersView
from .models import Project, UserProjectCompleted
from .serializer import ProjectModelSerializer, UserProjectCompletedSerializer


class ProjectModelViewSet(ModelViewSet):
    '''
    Класс который строит API для модели Project
    '''
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class UserProjectCompletedViewSet(ModelViewSet):
    '''
    Класс который строит API для модели UserProjectCompleted
    '''
    queryset = UserProjectCompleted.objects.all()
    serializer_class = UserProjectCompletedSerializer
