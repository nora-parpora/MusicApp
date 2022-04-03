from django.shortcuts import redirect, render

from Music_App_v2.main_app.forms import DeleteProfileForm
from Music_App_v2.main_app.models import Album
from Music_App_v2.main_app.views.general import get_profile


def profile_action(request, form_class, success_url, instance, template_name):
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect(success_url)
    else:
        form = form_class(instance=instance)

    context = {
        'form': form,

    }
    return render(request, template_name, context)


def delete_profile(request):
    return profile_action(request, DeleteProfileForm, 'index', get_profile(), 'profile-delete.html')


def profile_details(request):
    profile = get_profile()
    num_albums = len(Album.objects.all())

    context = {
        'profile': profile,
        'num_albums': num_albums,

    }
    return render(request, 'profile-details.html', context)
