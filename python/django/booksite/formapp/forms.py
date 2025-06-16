# pylint: disable=too-few-public-methods
"""Django ModelForms for formapp models."""

from django import forms
from .models import (
    Book, Car, Song, Movie, JobPosting,
    Product, Task, Post, Enrollment
)


class BookForm(forms.ModelForm):
    """Form for the Book model."""
    class Meta:
        """Meta class to define model and fields for the BookForm."""
        model = Book
        fields = "__all__"
    def __str__(self):
        return f"BookForm for {self.instance.title if self.instance.pk else 'New Book'}"


class CarForm(forms.ModelForm):
    """Form for the Car model."""
    class Meta:
        """Meta class to define model and fields for the CarForm."""
        model = Car
        fields = "__all__"
        widgets = {
            "transmission": forms.RadioSelect()
        }
    def __str__(self):
        return f"CarForm for {self.instance.title if self.instance.pk else 'New Car'}"


class SongForm(forms.ModelForm):
    """Form for the Song model."""
    class Meta:
        """Meta class to define model and fields for the SongForm."""
        model = Song
        fields = "__all__"


class MovieForm(forms.ModelForm):
    """Form for the Movie model."""
    class Meta:
        """Meta class to define model and fields for the MovieForm."""
        model = Movie
        fields = "__all__"


class JobPostingForm(forms.ModelForm):
    """Form for the JobPosting model."""
    class Meta:
        """Meta class to define model and fields for the JobPostingForm."""
        model = JobPosting
        fields = "__all__"


class ProductForm(forms.ModelForm):
    """Form for the Product model."""
    class Meta:
        """Meta class to define model and fields for the ProductForm."""
        model = Product
        fields = "__all__"


class TaskForm(forms.ModelForm):
    """Form for the Task model."""
    class Meta:
        """Meta class to define model and fields for the TaskForm."""
        model = Task
        fields = "__all__"


class PostForm(forms.ModelForm):
    """Form for the Post model."""
    class Meta:
        """Meta class to define model and fields for the PostForm."""
        model = Post
        fields = "__all__"

class EnrollmentForm(forms.ModelForm):
    """Form for the Enrollment model."""
    class Meta:
        """Meta class to define model and fields for the EnrollmentForm."""
        model = Enrollment
        fields = "__all__"
