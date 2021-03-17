from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import TrackForm


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
    success_url = reverse_lazy('tracks:list')
    template_name = 'tracks/song_form.html'
    

class CreateTrack(generic.CreateView):
    model = Track
    template_name = 'tracks/song_form.html'
    form_class = TrackForm
    success_url = reverse_lazy('tracks:list')


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
    
    
    
    
    