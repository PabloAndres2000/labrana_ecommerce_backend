from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from labrana_backend.apps.listelement.api.serializers.element import (
    ListSerializer,
)
from labrana_backend.apps.listelement.providers import element as element_providers
from labrana_backend.utils.constants import DATA_NOT_FOUND, SERVER_ERROR


class ElementViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    # GET: api/listelements/element/
    def list(self, request):
        elements = element_providers.get_all_elements()
        serializer = ListSerializer(elements, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET: api/listelements/element/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        element = element_providers.get_element_by_pk(pk=pk)
        if not element:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(element)
        return Response(serializer.data, status=status.HTTP_200_OK)
