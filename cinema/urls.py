from django.urls import path, include
from rest_framework import routers

from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieSessionViewSet,
    OrderViewSet,
    MovieListCreateView,
    MovieDetailView
)

router = routers.DefaultRouter()
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "genres/",
        GenreViewSet.as_view(),
        name="genre-list"
    ),
    path(
        "cinema_halls/",
        CinemaHallViewSet.as_view(),
        name="cinemahall-list"
    ),
    path(
        "actors/",
        ActorViewSet.as_view(),
        name="actor-list"
    ),
    path(
        "movies/",
        MovieListCreateView.as_view(),
        name="movie-list"
    ),
    path(
        "movies/<int:pk>/",
        MovieDetailView.as_view(),
        name="movie-detail"
    )
]

app_name = "cinema"
