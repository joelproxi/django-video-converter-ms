
from rest_framework.serializers import ModelSerializer

from core.models import VideoFile


class VideoFileSerialzer(ModelSerializer):
    class Meta:
        model = VideoFile
        fields = ('id', 'video', 'video_data')
        extra_kwargs = {
            'video_data': {'read_only': True}
        }
