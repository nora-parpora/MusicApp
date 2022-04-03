from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

from Music_App_v2.main_app.views.album import add_album, album_details, edit_album, delete_album
from Music_App_v2.main_app.views.general import show_home
from Music_App_v2.main_app.views.profile import profile_details, delete_profile

urlpatterns = [
    path('', show_home, name='index'),
    path('add/', add_album, name='add album'),
    path('album/details/<int:pk>/', album_details, name='album details'),
    path('album/edit/<int:pk>/', edit_album, name='edit album'),
    path('album/delete/<int:pk>/', delete_album, name='delete album'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/delete/', delete_profile, name='delete profile'),


] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)