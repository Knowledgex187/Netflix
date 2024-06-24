from django.urls import path
from . import views

""""<str:pk>/": This is a dynamic segment of the URL.
It matches any string and captures it as a keyword argument
named pk (primary key).

<str:pk>: This indicates that the captured part of the URL will be treated
as a string and assigned to the variable pk. The str converter ensures that
the value is treated as a string.

Trailing Slash: The trailing slash / ensures that the URL ends with a slash,
which is a convention in Django to signify the end of the URL path."""

urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    # Dynamic URLs
    path("movie/<str:pk>/", views.movie, name="movie"),
    path("my-list/", views.my_list, name="my-list"),
    path("add-to-list/", views.add_to_list, name="add-to-list"),
    path("search/", views.search_term, name="search"),
    path("genre/<str:pk>/", views.genre, name="genre"),
    path("faq/", views.faq, name="faq"),
]
