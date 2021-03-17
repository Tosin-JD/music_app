from django.db import models
from django.contrib.auth import get_user_model
from . import custom_models
from django.utils.text import slugify

# get the global user model
User = get_user_model()

# Create your models here.
class Album(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=1024)
    album_cover = models.ImageField(upload_to='album_cover/')
    artiste = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.user)


class Track(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    artiste = models.CharField(max_length=50)
    lyric = models.TextField(verbose_name='Lyrics', blank=True, null=True)
    genre = models.CharField(max_length=20)
    description = models.CharField(max_length=1024)
    audio_file = custom_models.AudioFileField(upload_to='tracks/')
    song_cover = models.ImageField(upload_to='song_covers/')
    likes = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{} by {}'.format(self.title, self.user)

    def get_likes(self):
        """
        Parameter: self
        Return: the total likes for a song
        """
        return self.likes
        
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify
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
    
    
    