from rest_framework import serializers

from users.models import CustomUser


class EmailSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()

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