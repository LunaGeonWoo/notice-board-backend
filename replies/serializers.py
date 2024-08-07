from rest_framework import serializers
from users.serializers import UserTinySerializer
from .models import Reply


class ReplySerializer(serializers.ModelSerializer):
    writer = UserTinySerializer(read_only=True)

    class Meta:
        model = Reply
        exclude = [
            "comment",
        ]
