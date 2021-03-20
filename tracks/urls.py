from django.urls import path

from .views import (CreateTrack,
                    UpdateTrack,
                    TrackList,
                    TrackDetail,
                    DeleteTrack,
                    like_unlike_song
                    )

app_name = 'tracks'

urlpatterns = [
        path('upload/', CreateTrack.as_view(), name='upload'),
        path('create/', CreateTrack.as_view(), name='create'),
        path('update/<slug>/', UpdateTrack.as_view(), name='update'),
        path('list/', TrackList.as_view(), name='list'),
        path('single/<slug>/', TrackDetail.as_view(), name='detail'),
        path('delete/<slug>/', DeleteTrack.as_view(), name='delete'),
        path('like/<slug>/', like_unlike_song, name='like'),
        
    ]

