from django.contrib import admin

from Music_App_v2.main_app.models import Profile, Album


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username',)


@admin.register(Album)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('album_name',)
