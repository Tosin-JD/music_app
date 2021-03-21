from rest_framework import serializers

from .models import Album, Track, Comment, Like


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'








