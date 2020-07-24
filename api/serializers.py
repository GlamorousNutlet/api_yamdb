from rest_framework import serializers

from users.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('email',)
        model = CustomUser
