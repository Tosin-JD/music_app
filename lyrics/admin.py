from django.contrib import admin
from .model import (Lyric,
                    Chorus,
                    Verse,
                    Bridge,
                    Refrain,
                    )

# Register your models here.
admin.site.register(Lyric)
admin.site.register(Chorus)
admin.site.register(Verse)
admin.site.register(Bridge)
admin.site.register(Refrain)

