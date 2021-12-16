from rest_framework.serializers import HyperlinkedModelSerializer
from .models import User


class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name',
                  'email', 'id_telegramm', 'rating', 'image', 'open_profile']
        