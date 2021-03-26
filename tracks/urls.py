from django.urls import path

from .views import (CreateTrack,
                    UpdateTrack,
                    TrackList,
                    TrackDetail,
                    DeleteTrack,
                    like_unlike_song,
                    
                    CreateComment,
                    DeleteComment,
                    UpdateComment,
                    DetailComment,
                    )
                    
from .api_views import (song_api,
                    song_detail_api,
                    TrackListAPI,
                    TrackDetailAPI,
                    TrackListCreateAPIView,
                    TrackDetailDestroyAPIView,
                    TrackViewSet,
                    
                    ) 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('tracks', TrackViewSet, basename='track')
app_name = 'tracks'

urlpatterns = [
        # urls for track
        path('upload/', CreateTrack.as_view(), name='upload'),
        path('create/', CreateTrack.as_view(), name='create'),
        path('update/<slug>/', UpdateTrack.as_view(), name='update'),
        path('list/', TrackList.as_view(), name='list'),
        path('single/<slug>/', TrackDetail.as_view(), name='single'),
        path('detail/<pk>/', TrackDetail.as_view(), name='detail'),
        path('delete/<slug>/', DeleteTrack.as_view(), name='delete'),
        path('like/<slug>/', like_unlike_song, name='like'),
        
        # urls for comments
        path('comment/', CreateComment.as_view(), name='comment'),
        path('comment/edit/<slug>/', UpdateComment.as_view(), name='comment_edit'),
        path('comment/detail/<slug>/', DetailComment.as_view(), name='comment_detail'),
        path('comment/delete/<slug>/', DeleteComment.as_view(), name='comment_delete'),
        

        path('api/', song_api, name='api'),
        path('api/<int:pk>/', song_detail_api, name='api_detail'),
        path('api-av/', TrackListAPI.as_view(), name='api_av'),
        path('api-av/<int:pk>/', TrackDetailAPI.as_view(), name='api_detail_av'),
        
        path('api-gn/', TrackListCreateAPIView.as_view(), name='api_detail_av'),
        path('api-gn/<int:pk>/', TrackDetailDestroyAPIView.as_view(), name='api_detail_av'),
    ]


urlpatterns += router.urls


