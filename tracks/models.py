import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from . import custom_models
from django.utils.text import slugify

# get the global user model
User = get_user_model()

# Create your models here.
class Album(models.Model):
    unique_num = models.CharField(max_length=1024)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    album_cover = models.ImageField(upload_to='album_cover/')
    artiste = models.CharField(max_length=50)
    slug = models.SlugField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.uploaded_by)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_item = '{} {}'.format(self.title, self.unique_num)
            self.slug = slugify(slug_item)
        super().save(*args, **kwargs)
    


class Track(models.Model):
    unique_num = models.UUIDField(default=uuid.uuid4, unique=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artiste = models.CharField(max_length=50)
    genre = models.CharField(max_length=20)
    description = models.CharField(max_length=1024)
    song_cover = models.ImageField(upload_to='song_covers/')
    audio_file = custom_models.AudioFileField(upload_to='tracks/')
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.uploaded_by)

    def get_audio_url(self):
        try:
            audio_url = self.audio_file.url
            os.path.exists(audio_url)
        except IOError:
            print("File not found")
        return audio_url
    
    def get_audio_size(self):
        if self.audio_file.size:
            return format(self.audio_file.size, '.2f')
        return

    def get_audio_duration(self):
        if self.audio_file.duration:
            return self.audio_file.duration
        return None

    def get_image_url(self):
        return self.song_cover.url

    def get_likes(self):
        """
        Parameter: self
        Return: the total likes for a song
        """
        return self.likes
    
    def increase_like(self):
        """
        Parameter: self
        Return: the total likes for a song
        """
        self.likes += 1
        self.save()
    
    def decrease_like(self):
        """
        Parameter: self
        Return: the total likes for a song
        """
        self.likes -= 1
        self.save()
    
    def get_absolute_url(self):
        return reverse('tracks', kwargs={'slug': self.slug})
    
    def size(self):
        audio_size = int(self.audio_file.size)/ (1024 * 1024)
        audio_size = int(audio_size)
        return '{}mb'.format(audio_size)
        
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_item = '{} {}'.format(self.title, self.unique_num)
            self.slug = slugify(slug_item)
        super().save(*args, **kwargs)
    
class AlbumTrack(Track):
    owner_album = models.ForeignKey('Album', on_delete=models.CASCADE)


class Like(models.Model):
    """model to record the songs and likes of a user on songs"""
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} likes {}.'.format(self.user.first_name, self.track)


class Comment(models.Model):
    """model for comments that users make on a song"""
    passtrack = models.ForeignKey(Track, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    