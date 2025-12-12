from rest_framework import serializers

from author.models import Author


class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = "__all__"
