from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for user model.
    """
    class Meta:
        model = User
        exclude = ('quiz', 'created_at', 'updated_at',)
        extra_kwargs = {
            'username': {'validators': []},
        }
