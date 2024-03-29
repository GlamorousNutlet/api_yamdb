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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'title', 'author', 'text', 'score', 'pub_date']
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Comment
