from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Project, UserProjectCompleted
from .serializer import ProjectModelSerializer, UserProjectCompletedSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class ProjectsList(APIView):

    def post(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectModelSerializer(projects, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProjectCompletedViewSet(ModelViewSet):
    queryset = UserProjectCompleted.objects.all()
    serializer_class = UserProjectCompletedSerializer
