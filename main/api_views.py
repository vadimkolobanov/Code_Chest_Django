from rest_framework.viewsets import ModelViewSet
from .models import Project, UserProjectCompleted
from .serializer import ProjectModelSerializer, UserProjectCompletedSerializer

class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class UserProjectCompletedViewSet(ModelViewSet):
    queryset = UserProjectCompleted.objects.all()
    serializer_class = UserProjectCompletedSerializer