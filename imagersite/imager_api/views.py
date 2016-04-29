from django.shortcuts import render
from rest_framework import generics
from imager_images.models import Photo
from imager_api.serializers import PhotoSerializer

# Create your views here.


class APIPhotoList(generics.ListAPIView):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    def get_queryset(self):
        queryset = super(APIPhotoList, self).get_queryset()
        user = self.request.user
        return queryset.filter(owner=user)
