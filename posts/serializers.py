from rest_framework import serializers
from .models import Post
from users.serializers import UserTinySerializer


class PostListSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()

    class Meta:
        model = Post
        fields = [
            "id",
            "writer",
            "title",
            "created_at",
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "detail",
            "writer",
        ]
