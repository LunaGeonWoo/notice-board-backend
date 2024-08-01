from rest_framework import serializers
from .models import Post
from users.serializers import UserTinySerializer


class PostListSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()
    likes_count = serializers.IntegerField(source="likes_count", read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "writer",
            "title",
            "views",
            "created_at",
            "likes_count",
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
