from rest_framework import serializers
from labrana_backend.apps.listelement.models import Element
from labrana_backend.apps.listelement.providers import category as category_providers
from labrana_backend.apps.listelement.providers import type as type_providers


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = [
            "id",
            "title",
            "url_clean",
            "description",
            "category",
            "type",
        ]


# class CreateSerializer(serializers.ModelSerializer):
    #title = serializers.CharField(max_length=255)
    #url_clean = serializers.CharField(max_length=255)
    #description = serializers.CharField(max_length=255)
    # category = serializers.PrimaryKeyRelatedField(
        # queryset=category_providers.get_all_categories())
    # type = serializers.PrimaryKeyRelatedField(
        # queryset=type_providers.get_all_types())
