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

# Special Character Syntax
SpecialSym = set("!£$%^&*()?@;:~`¬-=_+")


# Create your views here.
def home(request):
    return render(request, "index.html")


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


def logout(request):
    auth_logout(request)
    messages.info(request, "You have logged out!")
    return redirect("/")


def profiles(request):
    return render(request, "profiles.html")
