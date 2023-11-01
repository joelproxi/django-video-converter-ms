import json
import pika
from rest_framework import viewsets, status, exceptions
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from config.permissions import IsAuthencicatedAndOwner

from core.models import VideoFile
from core.serializers import VideoFileSerialzer


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()


class VideoFileViewSet(viewsets.ModelViewSet):
    parser_classes = [FormParser, MultiPartParser]
    queryset = VideoFile.objects.all()
    serializer_class = VideoFileSerialzer
    # permission_classes = [IsAuthencicatedAndOwner,]

    def create(self, request, *args, **kwargs):
        data = request.data
        if 2 < len(data['video']) < 0:
            raise exceptions.ValidationError("Check your video file")

        serializer = VideoFileSerialzer(data=data)
        serializer.is_valid(raise_exception=True)
        video = serializer.save(video_data=data['video'].file.read())
        message = {
            'video_id': str(video.id),
            'mp3_id': None,
            'email': "joel@g.com"
            # 'email': request.user_svc['email']
        }
        print(video)

        try:
            channel.queue_declare(queue='video', durable=True)
            channel.basic_publish(
                exchange="",
                routing_key='video',
                body=json.dumps(message),
                properties=pika.BasicProperties(
                    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
                )
            )
        except Exception as err:
            self.perform_destroy(video)
            print(err)
            raise exceptions.APIException("Internal server error")
        return Response(serializer.data, status=status.HTTP_201_CREATED)
