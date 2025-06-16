# pylint: disable=too-few-public-methods

"""Views for the formapp application."""
from django.shortcuts import render, redirect
from .forms import (
    BookForm, CarForm, SongForm, MovieForm,
    JobPostingForm, ProductForm, TaskForm,
    PostForm, EnrollmentForm
)


# Create your views here.
def form_success(request):
    """Render a success page after form submission."""
    return render(request, "formapp/success.html")


def add_form_view(request, form_class, template_name):
    """
    Generic view to handle form submission and rendering."""
    form = form_class(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("formapp:success")
    return render(request, template_name, {"form": form})


# Reusable views
def add_book(request):
    """View to add a book using the BookForm."""
    return add_form_view(request, BookForm, "formapp/add_book.html")


def add_car(request):
    """View to add a car using the CarForm."""
    return add_form_view(request, CarForm, "formapp/add_car.html")


def add_song(request):
    """View to add a song using the SongForm."""
    return add_form_view(request, SongForm, "formapp/add_song.html")


def add_movie(request):
    """View to add a movie using the MovieForm."""
    return add_form_view(request, MovieForm, "formapp/add_movie.html")


def add_job(request):
    """View to add a job posting using the JobPostingForm."""
    return add_form_view(request, JobPostingForm, "formapp/add_job.html")


def add_product(request):
    """View to add a product using the ProductForm."""
    return add_form_view(request, ProductForm, "formapp/add_product.html")


def add_task(request):
    """View to add a task using the TaskForm."""
    return add_form_view(request, TaskForm, "formapp/add_task.html")


def add_post(request):
    """View to add a post using the PostForm."""
    return add_form_view(request, PostForm, "formapp/add_post.html")


def add_enrollment(request):
    """View to add an enrollment using the EnrollmentForm."""
    return add_form_view(request, EnrollmentForm, "formapp/add_enrollment.html")
