
import io
import json
import tempfile
import moviepy.editor
import audioop

from django.db import connections

from rest_framework.decorators import api_view
from rest_framework.response import Response

from convert.models import Mp3File
from convert.serializers import Mp3FileSerializer


@api_view(['GET'])
def convert_video(request):
    with connections['video_convert'].cursor() as cursor:
        cursor.execute("SELECT * FROM core_videofile")
        data = dictfetchall(cursor)
        print(data)
    return Response(json.dumps({'detail': 'ok'}))


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def video_from_db(video_id):
    with connections['video_convert'].cursor() as cursor:
        cursor.execute(
            "SELECT * FROM core_videofile WHERE id = %s", [video_id])
        row = cursor.fetchone()
    return row


def start_convert(body, ch):
    tf = tempfile.NamedTemporaryFile()
    tmp_video = video_from_db(body['video_id'])
    print(tmp_video)
    # print(tmp_video[1].read())
    print('start converting video')
    video = bytes(tmp_video[2])

    tf.write(video)
    audio = moviepy.editor.VideoFileClip(tf.name).audio
    tf.close()
    print('start converting audio')
    tf_path = tempfile.gettempdir() + f'/{body["video_id"]}.mp3'
    audio.write_audiofile(tf_path)

    a_f = open(tf_path, 'rb')
    data = a_f.read()
    print(data)
    # # data = Mp3File.objects.create(audio=tf_path, audio_data=data)

    # serializer = Mp3FileSerializer(data=data)
    # serializer.is_valid(raise_exception=True)
    # video_data = serializer.save(video_data=data.file.read())


class Mp3Query:
    pass
