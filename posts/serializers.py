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
            "views",
            "likes_count",
            "created_at",
        ]


class PostDetailSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()

    class Meta:
        model = Post
        fields = "__all__"


class PostCreateSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "title",
            "detail",
            "writer",
        ]
