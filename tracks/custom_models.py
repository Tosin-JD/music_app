"""
custom model for audio field
"""

import os
import wave
from mutagen.mp3 import MP3
from django.conf import settings
import contextlib
from django.db.models.fields.files import FieldFile, FileField
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class AudioFieldFileHandler(FieldFile):
    """
    this class will handle the 
    audio file that is attached to
    the AudioFileField model
    """
    def __init__(self, instance, field, name):
        super().__init__(instance, field, name)
        self.instance = instance
        self.field = field
        self.storage = field.storage
        
    def _check_audio_file(self):
        """
        check if the audio is greater than
        7mb
        also check if extension is .mp3 or .wave
        """
        self._require_file
        file = self.storage
        if self:
            if self.size > 6*1024*1024:
                raise ValidationError("Audio file too large ( greater than 7mb )")
            if not os.path.splitext(self.name)[1] in [".mp3",".wav"]:
                raise ValidationError("Doesn't have proper extension")
        else:
            raise ValidationError("Coldn't read uploaded file")

    @property
    def duration(self):
        self._require_file
        audio = MP3(self)
        print(audio.info.length)
        song_duration = audio.info.length /60 - 0.12
        song_duration = format(song_duration, '.2f')
        result = '{}:{}'.format(song_duration[0], song_duration[2:])
        return result
        
    @property
    def size(self):
        try:
            audio_size = super().size / (1024 * 1024)
        except:
            print("File not found")
        else:
            return audio_size
    
    def save(self, *args, **kwargs):
        self._check_audio_file()
        super().save(*args, **kwargs)


class AudioFileField(FileField):
    """
    this class will handle the audio 
    file and all its attribute for 
    each audio_file that is attached to
    the model Track
    """
    attr_class = AudioFieldFileHandler
    description = _("Audio")
    
    def __init__(self, verbose_name=None, name=None, **kwargs):
        super().__init__(verbose_name, name, **kwargs)

    
    
    

