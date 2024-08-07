from rest_framework import serializers
from .models import Post, Reply
from users.serializers import UserTinySerializer


class PostListSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    num_of_reactions = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "writer",
            "views",
            "likes_count",
            "num_of_reactions",
            "created_at",
        ]

    def get_num_of_reactions(self, post):
        return post.get_num_of_reactions()


class PostDetailSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer()
    likes_count = serializers.IntegerField(source="likes.count", read_only=True)
    dislikes_count = serializers.IntegerField(source="dislikes.count", read_only=True)
    is_like = serializers.SerializerMethodField()
    is_dislike = serializers.SerializerMethodField()
    num_of_reactions = serializers.SerializerMethodField()
    is_mine = serializers.SerializerMethodField()

    class Meta:
        model = Post
        exclude = ["likes", "dislikes"]

    def get_is_like(self, post):
        return post.is_like(self.context["request"].user)

    def get_is_dislike(self, post):
        return post.is_dislike(self.context["request"].user)

    def get_num_of_reactions(self, post):
        return post.get_num_of_reactions()

    def get_is_mine(self, post):
        return post.writer == self.context["request"].user


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


class ReplySerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Reply
        exclude = [
            "comment",
        ]
