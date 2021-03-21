from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, JsonResponse 
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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

# Create your views here.
class TrackMixin(LoginRequiredMixin):
    model = Track
    form_class = TrackForm
    success_url = reverse_lazy('tracks:list')
    template_name = 'tracks/song_form.html'
    

class CreateTrack(TrackMixin, generic.CreateView):
    model = Track
    
    def post(self, request, *args, **kwargs):
        try:
            super().post(request, *args, **kwargs)
        except ValidationError:
            messages.add_message(request, messages.ERROR,
                                 'Audio file error.'
                                 )
            return render(request, 
                          template_name=self.template_name, 
                          context=self.get_context_data())
        else:
            return HttpResponseRedirect(self.success_url)
            
    def form_valid(self, form):
        form.instance.uploaded_by = self.request.user
        return super(CreateTrack, self).form_valid(form)


class UpdateTrack(TrackMixin, generic.UpdateView):
    pass

    
class TrackList(generic.ListView):
    model = Track
    paginated_by = 8
    template_name = 'tracks/song_list.html'


class TrackDetail(generic.DetailView):
    model = Track
    template_name = 'tracks/song_detail.html'


class DeleteTrack(generic.DeleteView):
    model = Track
    success_url = reverse_lazy('tracks:list')
    template_name = 'tracks/song_delete.html'
    
    
@login_required
def like_unlike_song(request, slug):
    """allow users to vote on any question
    return the page of the question list"""
    track = get_object_or_404(Track, slug=slug)
    try:
        like = Like.objects.get(track=track, user__exact=request.user)
    except Like.DoesNotExist:
        print("Someone liked a song.")
        like = None
    finally:
        if like:
            track.decrease_like()
            like.delete()
        else:
            track.increase_like()
            Like.objects.create(track=track, user=request.user)
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('tracks:detail', args=(track.slug, )))






