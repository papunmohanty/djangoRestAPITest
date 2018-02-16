from rest_framework import serializers

from . import models


class BlogSerializer(serializers.ModelSerializer):
    """
    this class is used to convert all data from a Blog model to JSON format
    """

    class Meta:
        fields = ('id', 'title', 'content', 'created_at', 'updated_at',)
        model = models.Blog
