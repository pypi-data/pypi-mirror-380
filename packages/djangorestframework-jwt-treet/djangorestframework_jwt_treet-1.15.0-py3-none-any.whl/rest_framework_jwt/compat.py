from django.contrib.auth import get_user_model
from typing import Any, Dict

from rest_framework import serializers


class Serializer(serializers.Serializer):
    @property
    def object(self) -> Dict[str, Any]:
        return self.validated_data


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        if "style" not in kwargs:
            kwargs["style"] = {"input_type": "password"}
        else:
            kwargs["style"]["input_type"] = "password"
        super(PasswordField, self).__init__(*args, **kwargs)


def get_username_field() -> str:
    try:
        username_field = get_user_model().USERNAME_FIELD
    except AttributeError:
        username_field = "username"

    return username_field


def get_username(user) -> str:
    try:
        username = user.get_username()
    except AttributeError:
        username = user.username

    return username
