from rest_framework import serializers
from manager_app.models import Channel


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        exclude = ("user",)
