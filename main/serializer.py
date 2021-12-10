from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, UserProjectCompleted

class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'level',
                  'programming_language', 'check', 'date_created',
                  'is_active']


class UserProjectCompletedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProjectCompleted
        fields = ['id', 'user', 'project']