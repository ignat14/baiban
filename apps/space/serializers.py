from rest_framework import serializers

from .models import Folder, List, Space


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = '__all__'


class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = '__all__'