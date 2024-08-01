from rest_framework import serializers
from .models import User


class UserTinySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
        ]
