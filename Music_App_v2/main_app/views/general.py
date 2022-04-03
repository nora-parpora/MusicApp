from django.http import HttpResponse
from django.shortcuts import render, redirect

from Music_App_v2.main_app.forms import CreateProfileForm
from Music_App_v2.main_app.models import Profile, Album


def get_profile():

    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return


def show_home(request):
    profile = get_profile()
    if profile:
        albums = Album.objects.all()
        available_albums = False
        if len(albums) > 0:
            available_albums = True
        context = {
            "profile": profile,
            "albums": albums,
            "available_albums": available_albums,
        }
        return render(request, "home-with-profile.html", context)

    if request.method == 'POST':
        form = CreateProfileForm(request.POST, instance=Profile())
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateProfileForm()

    context = {
        "form": form,
    }
    return render(request, "home-no-profile.html", context)

