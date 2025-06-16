"""Admin site registrations for formapp models."""

from django.contrib import admin

from .models import (
    Book,
    Car,
    Song,
    Movie,
    JobPosting,
    Category,
    Product,
    Project,
    Task,
    Post,
    Student,
    Course,
    Enrollment,
)

# Registering models with the Django admin site
admin.site.register(Book)
admin.site.register(Car)
admin.site.register(Song)
admin.site.register(Movie)
admin.site.register(JobPosting)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Post)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Enrollment)
