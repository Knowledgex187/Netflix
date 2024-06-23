# Validation module
from django.core.exceptions import ValidationError

# Django shortcuts module
from django.shortcuts import render, redirect

# imports admin user table into code and enables for user to be logged in
from django.contrib.auth.models import User

# Imports messages to catch errors responses
from django.contrib import messages

# Django function to validate if email is correct format
from django.core.validators import validate_email

# Imports authenticate and login modules
from django.contrib.auth import authenticate, login, logout as auth_logout

# Import database
from .models import Movie, MovieList

# Decorator for logged in users
from django.contrib.auth.decorators import login_required

# The re module provides a wide array of functions and tools to work with regular expressions. Regular expressions allow you to search, match, and manipulate strings based on specific patterns.
import re

#  JsonResponse is a convenient way to return JSON-encoded data in HTTP responses.
from django.http import JsonResponse

from django.shortcuts import get_object_or_404

# Special Character Syntax
SpecialSym = set("!£$%^&*()?@;:~`¬-=_+")


def home(request):

    # Retrieves all Movies name in the database
    movies = Movie.objects.all()

    # Passes data from the view to the template
    context = {
        "movies": movies,
    }
    return render(request, "index.html", context)


@login_required(login_url="login")
def my_list(request):
    # Query the MovieList model to get all entries where the owner_user is the current user
    movie_list = MovieList.objects.filter(owner_user=request.user)

    # Initialize an empty list to store the movies
    user_movie_list = []

    # Loop through each entry in the movie_list
    for movie in movie_list:
        # Append the movie object from each MovieList entry to the user_movie_list
        user_movie_list.append(movie.movie)

    # Create a context dictionary to pass the list of movies to the template
    context = {"movies": user_movie_list}

    # Render the 'my_list.html' template with the context data
    return render(request, "my_list.html", context)


@login_required(login_url="login")
def add_to_list(request):
    # Check if the request method is POST
    if request.method == "POST":
        # Retrieve the 'movie_id' from the POST data
        movie_url_id = request.POST.get("movie_id")

        # Define a regex pattern to match a UUID
        uuid_pattern = (
            r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}"
        )

        # Search for the UUID pattern within the movie_url_id
        match = re.search(uuid_pattern, movie_url_id)

        # Extract the matched UUID or set movie_id to None if no match found
        movie_id = match.group() if match else None

        if movie_id:
            # Use get_object_or_404 to retrieve the Movie object with the matched UUID
            # This will raise a 404 error if no matching Movie is found
            movie = get_object_or_404(Movie, uuid=movie_id)

            # Attempt to get or create a MovieList object with the given user and movie
            # `owner_user` is set to the current user, and `movie` is the retrieved Movie object
            movie_list, created = MovieList.objects.get_or_create(
                owner_user=request.user, movie=movie
            )

            # Prepare the response data based on whether a new MovieList entry was created
            if created:
                response_data = {
                    "status": "success",
                    "message": "Added ✓",
                }  # New entry created
            else:
                response_data = {
                    "status": "info",
                    "message": "Movie already in list",
                }  # Entry already exists

            # Return the response data as a JSON response
            return JsonResponse(response_data)
        else:
            # If the request method is not POST, return an error response with a 400 status code
            return JsonResponse(
                {"status": "error", "message": "Invalid request"}, status=400
            )


@login_required(login_url="login")
def movie(request, pk):

    # Movie_uuid is equal to primary key id
    movie_uuid = pk
    # uuid is the database field name
    movie_details = Movie.objects.get(uuid=movie_uuid)
    movie_all = Movie.objects.all()

    content = {
        "movie_details": movie_details,
        "movie_all": movie_all,
    }

    return render(request, "movie.html", content)


def login_view(request):
    if request.method == "POST":

        # Validates the fields used in the login form
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "").strip()

        # Validates user login
        user_login = authenticate(username=username, password=password)

        # Logs user in
        if user_login is not None:
            login(request, user_login)
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid!")
            return redirect("/")
    else:
        return render(request, "login.html")


def signup(request):
    # Retrieves data from signup form html
    if request.method == "POST":
        # .strip() removes any whitespace to prevent errors
        username = request.POST.get("username", "").strip()
        email = request.POST.get("email", "").strip()
        first_name = request.POST.get("first_name", "").strip()
        last_name = request.POST.get("last_name", "").strip()
        password = request.POST.get("password", "").strip()
        password1 = request.POST.get("password1", "").strip()

        if (
            not username
            or not email
            or not first_name
            or not last_name
            or not password
            or not password1
        ):
            messages.info(request, "All fields are required!")
            return redirect("signup")

        # Username must equal to email
        if username != email:
            messages.info(request, "Username must be equal to email!")
            return redirect("signup")

        # If password 1 and 2 don't match
        if password != password1:
            messages.info(request, "Passwords do not match!")
            return redirect("signup")

        # If user exists, state it does
        if User.objects.filter(username=username).exists():
            messages.info(request, "User already exists!")
            return redirect("signup")

        # Email length parameters
        if len(email) < 7:
            messages.info(request, "Email must be longer than 6 characters!")
            return redirect("signup")

        # Checks if email matches Django email requirements
        try:
            validate_email(email)
        except ValidationError:
            messages.info(request, "Invalid email format!")
            return redirect("signup")

        # First name length parameters
        if len(first_name) < 3:
            messages.info(
                request, "First Name must contain more than 2 characters!"
            )
            return redirect("signup")

        # First name letters only parameters
        if not first_name.isalpha():
            messages.info(request, "First Name must be letters only!")
            return redirect("signup")

        # Last name length parameters
        if len(last_name) < 3:
            messages.info(request, "Last Name must be more than 2 characters!")
            return redirect("signup")

        # Last name letters only parameters
        if not last_name.isalpha():
            messages.info(request, " Last Name must be letters only!")
            return redirect("signup")

        # Password Numerical value parameters
        if not any(char.isdigit() for char in password):
            messages.info(request, "Password must contain a numerical value!")
            return redirect("signup")

        # Password capital letter parameters
        if not any(char.isupper() for char in password):
            messages.info(request, "Password must contain a capital letter!")
            return redirect("signup")

        # Password Special Character parameters
        if not any(char in SpecialSym for char in password):
            messages.info(request, "Password must contain a special Character")
            return redirect("signup")

        #
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.save()

        # Authenticate and log the user in
        user_login = authenticate(username=username, password=password)
        if user_login:
            login(request, user_login)
            return redirect("/")
        else:
            messages.info(request, "Authentication failed!")
            return redirect("signup")

    return render(request, "signup.html")


@login_required(login_url="login")
def logout(request):
    auth_logout(request)
    messages.info(request, "You have logged out!")
    return redirect("/")


@login_required(login_url="login")
def profiles(request):
    return render(request, "profiles.html")
