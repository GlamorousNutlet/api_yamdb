from rest_framework import serializers

from users.models import CustomUser


class EmailSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()

    class Meta:
        fields = ('email',)
        model = CustomUser
