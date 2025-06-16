"""Models for various applications in a Django project."""
from django.db import models

# Create your models here.


class Book(models.Model):
    """Model representing a book in the library."""
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=13)


class Car(models.Model):
    """Model representing a car with various attributes."""
    TRANSMISSION_CHOICES = [
        ("Automatic", "Automatic"),
        ("Manual", "Manual"),
    ]
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)


class Song(models.Model):
    """Model representing a song with title, artist, genre, and duration."""
    GENRE_CHOICES = [
        ("Pop", "Pop"),
        ("Rock", "Rock"),
        ("Hip Hop", "Hip Hop"),
        ("Electronic", "Electronic"),
    ]
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=50)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    duration = models.FloatField()


class Movie(models.Model):
    """Model representing a movie with title, director, release year, and rating."""
    RATING_CHOICES = [
        ("G", "G"),
        ("PG", "PG"),
        ("PG-13", "PG-13"),
        ("R", "R"),
    ]
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=50)
    release_year = models.IntegerField()
    rating = models.CharField(max_length=10, choices=RATING_CHOICES)


class JobPosting(models.Model):
    """Model representing a job posting with title, company, location, and employment type."""
    EMPLOYMENT_CHOICES = [
        ("Full-time", "Full-time"),
        ("Part-time", "Part-time"),
        ("Contract", "Contract"),
    ]
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    employment_type = models.CharField(max_length=20, choices=EMPLOYMENT_CHOICES)


class Category(models.Model):
    """Model representing a category for products or posts."""
    name = models.CharField(max_length=50)


class Product(models.Model):
    """Model representing a product with name, description, and category."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Project(models.Model):
    """Model representing a project with name and description."""
    name = models.CharField(max_length=50)
    description = models.TextField()


class Task(models.Model):
    """Model representing a task with name, description, and associated project."""
    name = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)


class Post(models.Model):
    """Model representing a blog post with title, content, and category."""
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Student(models.Model):
    """Model representing a student with a name."""
    name = models.CharField(max_length=100)


class Course(models.Model):
    """Model representing a course with a name."""
    name = models.CharField(max_length=100)


class Enrollment(models.Model):
    """Model representing an enrollment of a student in a course."""
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=2)
