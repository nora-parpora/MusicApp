from django.shortcuts import redirect, render

from Music_App_v2.main_app.forms import AddAlbumForm, EditAlbumForm, DeleteAlbumForm
from Music_App_v2.main_app.models import Album


def album_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,
        'album': instance
    }
    return render(request, template_name, context)


def add_album(request):
    return album_action(request, AddAlbumForm, 'index', Album(), 'add-album.html')


def edit_album(request, pk):
    return album_action(request, EditAlbumForm, 'index', Album.objects.get(pk=pk), 'edit-album.html')


def delete_album(request, pk):
    return album_action(request, DeleteAlbumForm, 'index', Album.objects.get(pk=pk), 'delete-album.html')


def album_details(request, pk):
    album = Album.objects.get(pk=pk)
    available_description = False
    if album.description:
        available_description = True
    context = {
        'album': album,
        'available_description': available_description,
    }
    return render(request, 'album-details.html', context)

