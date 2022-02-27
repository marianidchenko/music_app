from django.shortcuts import render, redirect

from music_app.main.forms import CreateProfileForm, CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, DeleteProfileForm
from music_app.main.helpers import get_profile, get_albums, get_album_by_pk


def show_index(request):
    profile = get_profile()
    albums = get_albums()
    if profile:
        context = {
            'profile': profile,
            'albums': albums,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('show index')
        else:
            form = CreateProfileForm()
        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)


def show_album_create(request):
    if request.method == 'POST':
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = CreateAlbumForm()

    context = {
        'form': form,
    }
    return render(request, 'add-album.html', context)


def show_album_details(request, pk):
    album = get_album_by_pk(pk)
    context = {
        'album': album,
    }
    return render(request, 'album-details.html', context)


def show_album_edit(request, pk):
    album = get_album_by_pk(pk)
    if request.method == 'POST':
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = EditAlbumForm(instance=album)
    context = {
        'form': form,
    }
    return render(request, 'edit-album.html', context)


def show_album_delete(request, pk):
    album = get_album_by_pk(pk)
    if request.method == 'POST':
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteAlbumForm(instance=album)
    context = {
        'form': form,
    }
    return render(request, 'delete-album.html', context)


def show_profile_details(request):
    profile = get_profile()
    number_of_albums = len(get_albums())
    context = {
        'profile': profile,
        'number_of_albums': number_of_albums
    }
    return render(request, 'profile-details.html', context)


def show_profile_delete(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('show index')
    else:
        form = DeleteProfileForm(instance=profile)
    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)