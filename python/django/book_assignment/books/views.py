from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from .models import Profile, Author, Publisher, Book, Collection
from . import queries
from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Welcome to Book Project</h1><p>Visit /books/, /authors/, etc.</p>"
    )


# --------------------
# Profiles
# --------------------
class ProfileListView(ListView):
    template_name = "books/profile_list.html"
    context_object_name = "profiles"

    def get_queryset(self):
        return queries.get_all_profiles()


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "books/profile_detail.html"  # Or whatever template path you use


# --------------------
# Authors
# --------------------
class AuthorListView(ListView):
    template_name = "books/author_list.html"
    context_object_name = "authors"

    def get_queryset(self):
        return Author.objects.all()


class AuthorDetailView(DetailView):
    model = Author
    template_name = "books/author_detail.html"
    context_object_name = "author"


# --------------------
# Publishers
# --------------------
class PublisherListView(ListView):
    template_name = "books/publisher_list.html"
    context_object_name = "publishers"

    def get_queryset(self):
        return queries.get_all_publishers()


class PublisherDetailView(DetailView):
    model = Publisher
    template_name = "books/publisher_detail.html"
    context_object_name = "publisher"


# --------------------
# Books
# --------------------
class BookListView(ListView):
    template_name = "books/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        return Book.objects.all()


class BookDetailView(DetailView):
    model = Book
    template_name = "books/book_detail.html"
    context_object_name = "book"


# --------------------
# Collections
# --------------------
class CollectionListView(ListView):
    template_name = "books/collection_list.html"
    context_object_name = "collections"

    def get_queryset(self):
        return queries.get_all_collections()


class CollectionDetailView(DetailView):
    model = Profile
    template_name = "books/collection_detail.html"


# queries question
# 1. List All Author Names


def author_names_view(request):
    authors = queries.get_all_author_names()
    return render(request, "books/author_names.html", {"authors": authors})


# 2. List Author Name + Profile Details


def authors_with_profiles_view(request):
    data = queries.get_all_authors_with_profiles()
    return render(request, "books/authors_with_profiles.html", {"data": data})


# 3. Books by Authors Starting with 'a'


def books_by_author_starting_a_view(request):
    books = queries.get_books_by_author_name_starting_with_a()
    return render(request, "books/books_list.html", {"books": books})


# 4. Books by Given Author (use GET param)


def books_by_author_view(request):
    name = request.GET.get("name", "")
    books = queries.get_books_by_author_name(name)
    return render(request, "books/books_list.html", {"books": books})


# 5. Authors with More Than 2 Books


def authors_with_multiple_books_view(request):
    authors = queries.authors_with_more_than_two_books()
    return render(request, "books/authors_list.html", {"authors": authors})


# 6. Books by Author & Publisher (GET params)


def books_by_author_and_publisher_view(request):
    author = request.GET.get("author", "")
    publisher = request.GET.get("publisher", "")
    books = queries.get_books_by_author_and_publisher(author, publisher)
    return render(request, "books/books_list.html", {"books": books})


# 7. Books by Authors Ending with 'a'


def books_by_author_ending_a_view(request):
    books = queries.get_books_by_author_name_ending_with_a()
    return render(request, "books/books_list.html", {"books": books})


# 8. Books by Year


def books_by_year_view(request):
    year = request.GET.get("year")
    books = queries.get_books_by_publication_year(year)
    return render(request, "books/books_list.html", {"books": books})


# 9. Books by Publisher Name


def books_by_publisher_view(request):
    name = request.GET.get("name", "")
    books = queries.get_books_by_publisher_name(name)
    return render(request, "books/books_list.html", {"books": books})


# 10. Get or Create Book


def get_or_create_book_view(request):
    # You can test using hardcoded or GET params
    book_data = {
        "title": request.GET.get("title"),
        "author_id": request.GET.get("author_id"),
        "publisher_id": request.GET.get("publisher_id"),
        "date_of_pub": request.GET.get("date_of_pub"),
    }
    obj, created = queries.get_or_create_book(**book_data)
    return render(request, "books/book_detail.html", {"book": obj, "created": created})


# 11. Profile by Author Name


def profile_by_author_name_view(request):
    name = request.GET.get("name", "")
    authors = Author.objects.filter(name__iexact=name).select_related("profile")
    return render(request, "books/profiles.html", {"authors": authors})


# 12–13. Books by Publisher Name / Website


def books_by_publisher_website_view(request):
    website = request.GET.get("website", "")
    books = queries.get_books_by_publisher_website(website)
    return render(request, "books/books_list.html", {"books": books})


# 14. Author & Book Count Dictionary


def author_book_count_view(request):
    data = queries.get_author_book_count()
    return render(request, "books/author_book_count.html", {"data": data})


# 15. Books by Publisher List


def books_by_publishers_view(request):
    names = request.GET.getlist("names")
    books = queries.get_books_by_publisher_names(names)
    return render(request, "books/books_list.html", {"books": books})


# 16. Books by Author A or B


def books_by_authors_a_b_view(request):
    a1 = request.GET.get("a1")
    a2 = request.GET.get("a2")
    books = queries.get_books_by_two_authors(a1, a2)
    return render(request, "books/books_list.html", {"books": books})


# 17. Exclude Author


def books_excluding_author_view(request):
    name = request.GET.get("name", "")
    books = queries.get_books_excluding_author(name)
    return render(request, "books/books_list.html", {"books": books})


# 18. Delete Book


def delete_book_view(request, book_id):
    status = queries.delete_book_by_id(book_id)
    return render(request, "books/delete_status.html", {"status": status})


# 19–20. Soft Delete Book


def soft_delete_book_view(request, book_id):
    status = queries.soft_delete_book(book_id)
    return render(request, "books/delete_status.html", {"status": status})
