from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
)


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "name", "email", "password"]
