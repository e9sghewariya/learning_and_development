"""URL configuration for formapp views."""

from django.urls import path
from . import views

APP_NAME = "formapp"

urlpatterns = [
    path("book/", views.add_book, name="add_book"),
    path("car/", views.add_car, name="add_car"),
    path("song/", views.add_song, name="add_song"),
    path("movie/", views.add_movie, name="add_movie"),
    path("job/", views.add_job, name="add_job"),
    path("product/", views.add_product, name="add_product"),
    path("task/", views.add_task, name="add_task"),
    path("post/", views.add_post, name="add_post"),
    path("enrollment/", views.add_enrollment, name="add_enrollment"),
    path("success/", views.form_success, name="success"),
]
