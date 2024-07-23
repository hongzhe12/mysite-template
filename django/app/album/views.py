from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "album/pictures.html")


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm


def album_list(request):
    albums = Album.objects.all()
    return render(request, 'album/album_list.html', {'albums': albums})


def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        album.delete()
        return redirect('album:album_list')
    return render(request, 'album/delete_album.html', {'album': album})


def album_detail(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    photos = album.photos.all()
    return render(request, 'album/album_detail.html', {'album': album, 'photos': photos})


def add_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album:album_list')
    else:
        form = AlbumForm()
    return render(request, 'album/add_album.html', {'form': form})


def add_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('album:album_list')
    else:
        form = PhotoForm()
    return render(request, 'album/add_photo.html', {'form': form})
