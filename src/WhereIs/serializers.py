from rest_framework import serializers
from WhereIs.models import *


class RepositorioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepositorioModel
        fields = '__all__'


class ServidorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServidorModel
        fields = ('repositorios', 'ip', 'dominio')
