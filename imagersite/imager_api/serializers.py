from imager_images.models import Photo
from rest_framework import serializers


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('file', 'title', 'description', 'date_uploaded',
                  'date_modified', 'date_published', 'published')
