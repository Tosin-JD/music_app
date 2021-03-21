from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse 
from django.urls import reverse, reverse_lazy
from django.views import generic
from .forms import TrackForm

from rest_framework import viewsets
from rest_framework import generics as rest_generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TrackSerializer
# get the global user
from django.contrib.auth import get_user_model

from .models import (Track,
                    Album,
                    Like,
                    Track,
                    Comment
                    )



def song_api(request):
    MAX_OBJECTS = 8
    track = Track.objects.all()[:MAX_OBJECTS]
    data = {"results": list(track.values('uploaded_by', 'title', 'artiste'))}
    return JsonResponse(data)


def song_detail_api(request, pk):
    track = get_object_or_404(Track, pk=pk)
    data = {"results": {
        'uploaded_by': track.uploaded_by.first_name,
        'title': track.title,
        'artiste': track.artiste,
    }}
    return JsonResponse(data)


class TrackListAPI(APIView):
    def get(self, request):
        track = Track.objects.all()[:8]
        data = TrackSerializer(track, many=True).data
        return Response(data)


class TrackDetailAPI(APIView):
    def get(self, request, pk):
        track = get_object_or_404(Track, pk=pk)
        data = TrackSerializer(track).data
        return Response(data)


class TrackListCreateAPIView(rest_generics.ListCreateAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class TrackDetailDestroyAPIView(rest_generics.RetrieveDestroyAPIView):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    

class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()[:8]
    serializer_class = TrackSerializer

