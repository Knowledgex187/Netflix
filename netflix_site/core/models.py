from django.db import models

# Imports UUID Module
import uuid

# Create your models here.


class Movie(models.Model):

    GENRE_CHOICES = [
        ("ACTION", "Action"),
        ("COMEDY", "Comedy"),
        ("DRAMA", "Drama"),
        ("HORROR", "Horror"),
        ("ROMANCE", "Romance"),
        ("SCIENCE_FICTION", "Science Fiction"),
        ("FANTASY", "Fantasy"),
    ]

    RATING = [
        ("U", "U"),
        ("PG", "PG"),
        ("12", "12"),
        ("15", "15"),
        ("18", "18"),
    ]

    # This field stores a universally unique identifier
    uuid = models.UUIDField(default=uuid.uuid4)
    # This field stores a short text, in this case, the title of the movie.
    title = models.CharField()
    # This field is intended to store a description of the movie.
    description = models.TextField()
    # This field stores the names of the main actors or stars of the movie.
    stars = models.CharField()
    # This field stores the release date of the movie in date format (YYYY-MM-DD).
    release_date = models.DateField()
    # This field stores the genre of the movie.
    genre = models.CharField(choices=GENRE_CHOICES)
    # Rating
    rating = models.CharField(choices=RATING, default="U")
    # This field stores the length of the movie in minutes.
    length = models.PositiveIntegerField()
    # This field stores the name of the director of the movie.
    director = models.CharField()
    # This field stores the name of the producer of the movie.
    produced_by = models.CharField()
    # This field stores the name(s) of the writer(s) of the movie.
    writers = models.CharField()
    # This field is for storing an image associated with the movie, typically a small thumbnail or card image.
    image_card = models.ImageField(upload_to="media/images/")
    # This field is for storing a larger cover image for the movie.
    image_cover = models.ImageField(upload_to="media/images/")
    # This field stores a video file of the movie.
    video = models.FileField(upload_to="media/")
    # This field keeps track of the number of views the movie has received.
    movie_views = models.IntegerField(default=0)

    # This returns the title of the movie. This is useful for displaying the movie title in Django admin or when the object is printed in other contexts.
    def __str__(self):
        return self.title
