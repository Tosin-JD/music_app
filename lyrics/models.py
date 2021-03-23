import uuid
from tracks.models import Track
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Lyric(models.Model):
    unique_num = models.UUIDField(default=uuid.uuid4, unique=True)
    uploaded_by = models.models.ForeignKey(User, on_delete=models.SET_NULL)
    track = models.OneToOneField(Track, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=144)
    slug = models.SlugField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} by {}'.format(self.title, self.uploaded_by)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug_item = '{} {}'.format(self.title, self.unique_num)
            self.slug = slugify(slug_item)
        super().save(*args, **kwargs)


class Chorus(models.Model):
    lyric = models.OneToOneField(Lyric, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Verse(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Bridge(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class Refrain(models.Model):
    lyric = models.ForeignKey(Lyric, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text
