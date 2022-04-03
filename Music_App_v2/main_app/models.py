from django.core.validators import MinLengthValidator
from django.db import models

from Music_App_v2.main_app.validators import validate_only_letters_nums_underscore, validate_only_positive_numbers, \
     validate_age_has_only_positive_integers


class Profile(models.Model):
    MIN_LENGTH = 2
    MAX_LENGTH = 15
    username = models.CharField(
        max_length=MAX_LENGTH,
        validators=(
            MinLengthValidator(MIN_LENGTH),
            validate_only_letters_nums_underscore,
        ))
    email = models.EmailField()
    age = models.IntegerField(
        blank=True,
        null=True,
        validators=(
            validate_age_has_only_positive_integers,
        ))



class Album(models.Model):
    POP_MUSIC = "Pop Music"
    JAZZ_MUSIC = "Jazz Music"
    R_B_MUSIC = "R&B Music"
    ROCK_MUSIC = "Rock Music"
    COUNTRY_MUSIC = "Country Music"
    DANCE_MUSIC = "Dance Music"
    HIP_HOP_MUSIC = "Hip Hop Music"
    OTHER = "Other"

    TYPES = [(x, x) for x in (POP_MUSIC, JAZZ_MUSIC, R_B_MUSIC, ROCK_MUSIC, COUNTRY_MUSIC, DANCE_MUSIC, HIP_HOP_MUSIC, OTHER)]

    album_name = models.CharField(
        max_length=30,
        unique=True, verbose_name="Album Name")
    artist = models.CharField(
        max_length=30,
    )
    genre = models.CharField(
        max_length=30,
        choices=TYPES,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    image_url = models.URLField(
        verbose_name= "Image URL"
    )
    price = models.FloatField(
        validators=(
            validate_only_positive_numbers,
        )
    )
