from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, UserProjectCompleted
from rest_framework import serializers


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'level',
                  'programming_language', 'check', 'date_created',
                  'is_active']

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class UserProjectCompletedSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserProjectCompleted
        fields = ['id', 'user', 'project']
