""" Views for the library application."""
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Author, Book

# Create your views here.

#Author Views

class AuthorListView(ListView):
    """View to list all authors."""
    model = Author


class AuthorCreateView(CreateView):
    """View to create a new author."""
    model = Author
    fields = ['name', 'birth_year']

class AuthorUpdateView(UpdateView):
    """View to update an existing author."""
    model = Author
    fields = ['name', 'birth_year']
    success_url = reverse_lazy('author-list')

class AuthorDeleteView(DeleteView):
    """View to delete an author."""
    model = Author
    success_url = reverse_lazy('author-list')

#Book Views

class BookListView(ListView):
    """View to list all books."""
    model = Book

class BookCreateView(CreateView):
    """View to create a new book."""
    model = Book
    fields = ['title', 'author', 'published_year']
    success_url = reverse_lazy('book-list')

class BookUpdateView(UpdateView):
    """View to update an existing book."""
    model = Book
    fields = ['title', 'author', 'published_year']
    success_url = reverse_lazy('book-list')

class BookDeleteView(DeleteView):
    """View to delete a book."""
    model = Book
    success_url = reverse_lazy()

