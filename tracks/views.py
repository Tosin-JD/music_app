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


class CreateComment(generic.CreateView):
    model = Comment
    fields = ('text',)
    
    def get_success_url(self):
        return reverse_lazy('tracks:single', args=[self.object.track.slug])

    def get_context_data(self, **kwargs):
        self.track = get_object_or_404(Track, id=self.kwargs['country_id'])
        kwargs['track'] = self.track
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        self.track = get_object_or_404(Track, slug=self.kwargs['slug'])
        form.instance.user = self.request.user
        form.instance.track = self.track
        messages.success(self.request, 'Your comment has been successfully added, thank you') 
        return super(CreateComment, self).form_valid(form)

class DetailComment(generic.DetailView):
    model = Comment
    fields = ('text',)
    

class UpdateComment(generic.UpdateView):
    model = Comment
    fields = ('text',)
    
    def get_success_url(self, kwargs):
        return reverse_lazy('tracks:list')


class DeleteComment(generic.DeleteView):
    model = Comment

    def get_success_url(self, kwargs):
        return reverse_lazy('tracks:list')





