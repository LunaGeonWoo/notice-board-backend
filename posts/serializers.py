from rest_framework import serializers
from .models import Post
from users.serializers import UserTinySerializer


class PostListSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)

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
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    dislikes_count = serializers.IntegerField(source="dislikes.count", read_only=True)

    class Meta:
        model = Post
        exclude = ["likes", "dislikes"]


class PostCreateSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "detail",
            "writer",
        ]
