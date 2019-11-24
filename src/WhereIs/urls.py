from django.urls import path, include
from rest_framework import routers
from WhereIs.views import ServidorViewSet, RepositorioViewSet


router = routers.DefaultRouter()
router.register(r'servidores', ServidorViewSet)
router.register(r'repositorios', RepositorioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
]
