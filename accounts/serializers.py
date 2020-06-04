from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'country',
            'member',
            'groups',
            'user_permissions',
            'is_superuser',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login'
        ]
