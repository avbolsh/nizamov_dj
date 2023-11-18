import uuid
from .models import CustomUser
from rest_framework import serializers


class CustomUserSerilizer(serializers.ModelSerializer):

    id = serializers.UUIDField(default=uuid.uuid4)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["id", "username", "snils", "inn",  "birthday", "password"]

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validate_data):
        user = super().update(instance, validate_data)
        try:
            user.set_password(validate_data["password"])
        except KeyError:
            pass
        return user 