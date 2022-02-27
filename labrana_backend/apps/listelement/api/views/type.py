from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from labrana_backend.apps.listelement.api.serializers.type import (
    ListSerializer,
)
from labrana_backend.apps.listelement.providers import type as type_providers
from labrana_backend.utils.constants import DATA_NOT_FOUND, SERVER_ERROR


class TypeViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    # GET: api/listelements/type/
    def list(self, request):
        types = type_providers.get_all_types()
        serializer = ListSerializer(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET: api/listelements/type/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        type = type_providers.get_type_by_pk(pk=pk)
        if not type:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(type)
        return Response(serializer.data, status=status.HTTP_200_OK)
