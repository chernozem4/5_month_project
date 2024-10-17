from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from users.models import ConfirmationToken


class UserBaseValidateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField()

    def validate_password(self, password):
        return password
    def validate_username(self, username):
        try:
            User.objects.get(username = username)
        except:
            return username
        raise ValidationError('User already exists!')



class UserAuthSerializers(UserBaseValidateSerializer):
    pass





class UserCreateSerializer(UserBaseValidateSerializer):
    pass

class UserConfirmSerializer(UserBaseValidateSerializer):

    def validate(self, data):
        token = data.get('token')
        try:
            confirm_token = ConfirmationToken.objects.get(token=token)
            confirm_token.user.is_active = True
            confirm_token.user.save()
            confirm_token.delete()
        except ConfirmationToken.DoesNotExist:
            raise serializers.ValidationError("Invalid token")
        return data