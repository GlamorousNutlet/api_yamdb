from rest_framework import serializers

from users.models import CustomUser


class EmailSerializer(serializers.ModelSerializer):
    # token = serializers.SerializerMethodField()

    class Meta:
        fields = ('email',)
        model = CustomUser

#
# class JwtSerializer(serializers.ModelSerializer):
#     token = serializers.CharField(max_length=255, read_only=True)
#
#     class Meta:
#