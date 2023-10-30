from rest_framework import serializers

from core.models import UserModel


class UserModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        if password:
            user = UserModel.objects.create(**validated_data)
            user.set_password(password)
            user.save()
            return user
        return super().create(validated_data)
