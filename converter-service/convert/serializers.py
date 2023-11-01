from rest_framework.serializers import ModelSerializer

from convert.models import Mp3File


class Mp3FileSerializer(ModelSerializer):

    class Meta:
        model = Mp3File
        fields = ('id', 'audio',)
