from django.contrib import admin
from manager_app.models import Channel

# Register your models here.


@admin.register(Channel)
class ChannelaAdmin(admin.ModelAdmin):
    list_display = ("name", "channel_id", "date_add", "active")
    list_filter = ("active", "date_add")
    list_editable = ("active",)
    search_fields = ("name", "channel_id")
