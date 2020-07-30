from rest_framework import serializers

from .models import *


class EmailSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('email',)
        model = CustomUser


class CustomUserSerializers(serializers.ModelSerializer):

    class Meta:
        fields = (
            'first_name',
            'last_name',
            'username',
            'bio',
            'email',
            'role'
        )
        model = CustomUser
