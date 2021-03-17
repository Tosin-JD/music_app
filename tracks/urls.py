from django.urls import path

from .views import (CreateTrack,
                    UpdateTrack,
                    TrackList,
                    TrackDetail,
                    DeleteTrack,
                    )

app_name = 'tracks'

urlpatterns = [
        path('upload/', CreateTrack.as_view(), name='upload'),
        path('create/', CreateTrack.as_view(), name='create'),
        path('<slug>/update/', UpdateTrack.as_view(), name='update'),
        path('list/', TrackList.as_view(), name='list'),
        path('<slug>/detail/', TrackDetail.as_view(), name='detail'),
        path('<slug>/delete/', DeleteTrack.as_view(), name='delete'),
        
    ]

