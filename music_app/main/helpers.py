from music_app.main.models import Profile, Album


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def get_albums():
    albums = Album.objects.all()
    return albums


def get_album_by_pk(pk):
    album = Album.objects.get(pk=pk)
    return album

