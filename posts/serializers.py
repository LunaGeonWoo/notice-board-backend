from rest_framework import serializers
from .models import Post, Comment
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
    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ["likes", "dislikes"]

    def get_is_like(self, post):
        return post.is_like(self.context["request"].user)

    def get_is_dislike(self, post):
        return post.is_dislike(self.context["request"].user)


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


class CommentSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Comment
        exclude = [
            "post",
        ]
