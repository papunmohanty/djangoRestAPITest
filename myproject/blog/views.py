# from django.shortcuts import render

from rest_framework import generics
from . import serializers
from . import models


class BlogList(generics.ListAPIView):
    """
    this class based generic view is to list all Blog model details in JSON
    format
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    this class based generic view set is to show the detailed view
    for each database entry in JSON
    format
    """
    queryset = models.Blog.objects.all()
    serializer_class = serializers.BlogSerializer
