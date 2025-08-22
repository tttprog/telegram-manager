from django.urls import path
from manager_app.views import channel_list, add_channel

urlpatterns = [
    path(
        "channel-list/",
        channel_list,
        name="channel_list",
    ),
    path(
        "add-channel/",
        add_channel,
        name="add_channel",
    ),
]
