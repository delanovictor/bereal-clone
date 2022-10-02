import boto3
from datetime import datetime
from decouple import config

from feed.models import *
from feed.api.serializer import *

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def get_permissions(self):
        self.permission_classes = [IsAuthenticated, ]

        return super(PostViewSet, self).get_permissions()

    def get_queryset(self):
        queryset = Post.objects.all()

        person_id = self.request.query_params.get('person')

        if person_id is not None:
            queryset = queryset.filter(person=person_id)

        return queryset

    # Método que é chamado após o POST
    def create(self, request, *args, **kwargs):
        # Compartamento padrão do método create
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # Adiciona url de upload ao objeto de resposta
        post_data = serializer.data
        post_data['url'] = get_image_url(serializer.data)

        return Response(post_data, status=status.HTTP_201_CREATED, headers=headers)


# TODO: Achar o lugar correto para colocar essa função
def get_image_url(user_data):

    s3_client = boto3.client(
        's3',
        aws_access_key_id=config("AWS_USER"),
        aws_secret_access_key=config("AWS_SECRET")
    )

    dt = datetime.now()
    ts = datetime.timestamp(dt)

    # /{user}/{timestamp}.{ext}
    file_key = str(user_data['person']) + '/' + str(int(ts)) + '.' + 'jpg'

    upload_url = s3_client.generate_presigned_url(
        'put_object',
        Params={
            'Bucket': config("IMAGE_STORAGE"),
            'Key': file_key,
            'ContentType': 'image/jpg',
        },
        ExpiresIn=60
    )

    return upload_url
