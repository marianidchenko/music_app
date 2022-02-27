from django.contrib import admin

# Register your models here.
from music_app.main.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass

