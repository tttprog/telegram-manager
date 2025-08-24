from rest_framework import serializers
from django.core import validators
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password


class UserRegisterationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True,
        validators=[
            validators.RegexValidator(
                code="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                message="Password must be at least 8 characters long, include uppercase, lowercase, a digit, and a special character.",
            )
        ],
    )
    confirm_password = serializers.CharField(
        write_only=True,
        validators=[
            validators.RegexValidator(
                code="^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$",
                message="Password must be at least 8 characters long, include uppercase, lowercase, a digit, and a special character.",
            )
        ],
    )

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("Passwords is not match.")
        return data

    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Already Email is exists.")
        return value

    def create(self, validated_data):
        validated_data.pop("confirm_password", None)
        validated_data["password"] = make_password(validated_data["password"])
        return get_user_model().objects.create(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
