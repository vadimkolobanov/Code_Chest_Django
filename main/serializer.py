from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, UserProjectCompleted



class ProjectModelSerializer(HyperlinkedModelSerializer):
    '''
    Класс-сериализатор, который переводит объект Django модели Projects в JSON и
    обратно из JSON  в объект Django модели Projects.
    '''

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'level',
                  'programming_language', 'check', 'date_created', 'id_telegram', 'username',
                  'is_active']

    def create(self, validated_data):
        return Project.objects.create(**validated_data)


class UserProjectCompletedSerializer(HyperlinkedModelSerializer):
    '''
    Класс-сериализатор, который переводит объект Django модели UserProjectCompleted в JSON и
    обратно из JSON  в объект Django модели UserProjectCompleted.
    '''

    class Meta:
        model = UserProjectCompleted
        fields = ['id', 'user', 'project']
