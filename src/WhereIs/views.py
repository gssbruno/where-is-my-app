from rest_framework import viewsets
from WhereIs.serializers import ServidorSerializer, RepositorioSerializer
from WhereIs.models import ServidorModel, RepositorioModel


class ServidorViewSet(viewsets.ModelViewSet):
    queryset = ServidorModel.objects.all()
    serializer_class = ServidorSerializer


class RepositorioViewSet(viewsets.ModelViewSet):
    queryset = RepositorioModel.objects.all()
    serializer_class = RepositorioSerializer
