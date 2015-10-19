from rest_framework import serializers
from boxing.api.models import *

class ContainerSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Container
                fields = ('url', 'id', 'name', 'created', 'updated')

class ItemSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
                model = Item
                fields = ('url', 'id', 'name', 'image', 'container', 'created', 'updated')
