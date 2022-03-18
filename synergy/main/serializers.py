from .models import *
from rest_framework import serializers

"""serializer for user templates """


class CreateUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatedUsers
        fields = ['username', 'groups']


"""serializer for groups templates"""


class CreateGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreatedGroup
        fields = ['group']
