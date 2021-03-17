from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Track
import os 


# create the forms here
class TrackForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class':'form-control'})
        self.fields['artiste'].widget.attrs.update({'class':'form-control'})
        self.fields['genre'].widget.attrs.update({'class':'form-control'})
        self.fields['lyric'].widget.attrs.update({'class':'form-control'})
        self.fields['description'].widget.attrs.update({'class':'form-control'})
        self.fields['audio_file'].widget.attrs.update({'class':'form-control'})
        self.fields['song_cover'].widget.attrs.update({'class':'form-control'})
        
    class Meta:
        model = Track
        fields = ('title', 
                  'artiste',
                  'genre',
                  'lyric',
                  'description',
                  'audio_file',
                  'song_cover'
                 )
             
             
             
             
             
                 