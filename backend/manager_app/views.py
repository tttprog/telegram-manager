from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import response, status
from rest_framework import permissions
from manager_app.models import Channel
from manager_app.serializres import ChannelSerializer

# Create your views here.


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticated])
def channel_list(request):
    user = request.user
    channels = Channel.objects.filter(user=user).all()
    serializer = ChannelSerializer(channels, many=True)
    return response.Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def add_channel(request):
    user = request.user
    pass
