from rest_framework import serializers
from labrana_backend.apps.listelement.models import Category


class ListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "title",
            "url_clean",
        ]
