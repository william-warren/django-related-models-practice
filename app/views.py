from django.shortcuts import render, redirect
from app.models import Album, Song

# Renders home page with all albums loaded from database
# and returned in the context.

def album_list(request):
    album_list = Album.objects.all()
    return render(request, "album_list.dhtml", {"albums": album_list})


# Renders the single ablum view page with the selected
# album returned in the context.

def album_detail(request, id):
    album = Album.objects.get(id=id)
    return render(request, "album_detail.dhtml", {"album": album})


# Allows user to create a new song to be add to the album they are currently
# viewing.

def new_song(request, id):
    title = request.POST.get("title")
    seconds = request.POST.get("seconds")
    album = Album.objects.get(id=id)
    album.song_set.create(
        title=title,
        seconds=seconds
    )
    return redirect(f"/album/{id}")

