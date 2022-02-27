from rest_framework import serializers
from labrana_backend.apps.listelement.models import Type


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = [
            "id",
            "title",
            "url_clean",
        ]
