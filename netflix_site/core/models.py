from django.db import models
import uuid
from django.conf import settings


# Define the Movie model
class Movie(models.Model):
    # Choices for genre
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Horror", "Horror"),
        ("Romance", "Romance"),
        ("Fiction", "Fiction"),
        ("Fantasy", "Fantasy"),
    ]

    # Choices for rating
    RATING = [
        ("U", "U"),
        ("PG", "PG"),
        ("12", "12"),
        ("15", "15"),
        ("18", "18"),
    ]

    # Field to store a universally unique identifier for the movie
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # Field to store the title of the movie
    title = models.CharField(max_length=255)
    # Field to store a description of the movie
    description = models.TextField()
    # Field to store the names of the main actors or stars of the movie
    stars = models.CharField(max_length=255)
    # Field to store the release date of the movie
    release_date = models.DateField()
    # Field to store the genre of the movie, with choices defined above
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    # Field to store the rating of the movie, with choices defined above and a default value of "U"
    rating = models.CharField(max_length=2, choices=RATING, default="U")
    # Field to store the length of the movie in minutes
    length = models.PositiveIntegerField()
    # Field to store the name of the director of the movie
    director = models.CharField(max_length=255)
    # Field to store the name of the producer of the movie
    produced_by = models.CharField(max_length=255)
    # Field to store the names of the writers of the movie
    writers = models.CharField(max_length=255)
    # Field to store a small image (thumbnail) for the movie
    image_card = models.ImageField(upload_to="media/images/")
    # Field to store a larger cover image for the movie
    image_cover = models.ImageField(upload_to="media/images/")
    # Field to store a video file of the movie
    video = models.FileField(upload_to="media/")
    # Field to keep track of the number of views the movie has received
    movie_views = models.IntegerField(default=0)

    # String representation of the model, returning the title of the movie
    def __str__(self):
        return self.title


# Define the MovieList model, representing a list of movies for a user
class MovieList(models.Model):
    # Foreign key to the user model, indicating which user owns this movie list
    owner_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    # Foreign key to the movie model, linking each list entry to a movie
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
