from django.contrib import admin
from accounts_app.models import CustomUser
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    pass
