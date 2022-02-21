from rest_framework import serializers
from labrana_backend.apps.listelement.models import Element


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        models = Element
        fields = [
            "id",
            "title",
        ]
