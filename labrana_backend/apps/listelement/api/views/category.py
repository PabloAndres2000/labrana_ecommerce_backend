from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from labrana_backend.apps.listelement.api.serializers.category import (
    ListSerializer,
)
from labrana_backend.apps.listelement.providers import category as category_providers
from labrana_backend.utils.constants import DATA_NOT_FOUND, SERVER_ERROR


class CategoryViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    # GET: api/listelements/category/
    def list(self, request):
        categories = category_providers.get_all_categories()
        serializer = ListSerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # GET: api/listelements/category/<pk>/
    def retrieve(self, request, pk):
        if not pk:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        category = category_providers.get_category_by_pk(pk=pk)
        if not category:
            return Response(DATA_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)
        serializer = ListSerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
