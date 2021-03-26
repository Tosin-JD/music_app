from django.contrib import admin
from .models import (Album,
                    Comment,
                    Genre,
                    Like,
                    Track,

                    )


# Register your models here.
admin.site.register(Album)
admin.site.register(Comment)
admin.site.register(Genre)
admin.site.register(Like)
admin.site.register(Track)

