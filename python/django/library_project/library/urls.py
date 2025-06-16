"""Library URL Configuration
This module defines the URL patterns
 for the library application, 
 including routes for authors and books.
"""

from django.urls import path
from .views import (
    AuthorListView,
    AuthorCreateView,
    AuthorUpdateView,
    AuthorDeleteView,
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    # Author urls
    path("authors/", AuthorListView.as_view(), name="author-list"),
    path("authors/add/", AuthorCreateView.as_view(), name="author-add"),
    path("authors/<int:pk>/update/", AuthorUpdateView.as_view(), name="author-edit"),
    path("authors/<int:pk>/delete/", AuthorDeleteView.as_view(), name="author-delete"),
    # Book Urls
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/add/", BookCreateView.as_view(), name="book-add"),
    path("books/<int:pk>/update/", BookUpdateView.as_view(), name="book-edit"),
    path("books/<int:pk>/delete/", BookDeleteView.as_view(), name="book-delete"),
]
