from rest_framework import serializers
from users.serializers import UserTinySerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)
    replies_count = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        exclude = [
            "post",
        ]

    def get_replies_count(self, comment):
        return comment.replies.count()
