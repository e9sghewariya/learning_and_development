from django.db.models import Count, Q
from .models import Profile, Author, Publisher, Book, Collection


# ------------------------------
# Profile Queries
# ------------------------------


def get_all_profiles():
    return Profile.objects.all()


def get_profile_by_email(email):
    return Profile.objects.get(email=email)


# ------------------------------
# Author Queries
# ------------------------------


def get_all_author_names():
    return list(Author.objects.values_list("name", flat=True))


def get_all_authors_with_profiles():
    return Author.objects.select_related("profile").values(
        "name", "profile__phone", "profile__address"
    )


def authors_with_more_than_two_books():
    return Author.objects.annotate(book_count=Count("books")).filter(book_count__gt=2)


# ------------------------------
# Publisher Queries
# ------------------------------


def get_all_publishers():
    return Publisher.objects.all()


def get_publisher_by_name(name):
    return Publisher.objects.get(name=name)


# ------------------------------
# Book Queries
# ------------------------------


def get_books_by_author_name_starting_with_a():
    return Book.objects.filter(author__name__istartswith="a")


def get_books_by_author_name(name):
    return Book.objects.filter(author__name=name)


def get_books_by_author_and_publisher(author_name, publisher_name):
    return Book.objects.filter(author__name=author_name, publisher__name=publisher_name)


def get_books_by_author_name_ending_with_a():
    return Book.objects.filter(author__name__iendswith="a")


def get_books_by_publication_year(year):
    return Book.objects.filter(date_of_pub__year=year)


def get_books_by_publisher_name(name):
    return Book.objects.filter(publisher__name=name)


def get_books_by_publisher_website(website):
    return Book.objects.filter(publisher__website=website)


def get_books_by_publisher_names(names):
    return Book.objects.filter(publisher__name__in=names)


def get_books_by_two_authors(author1, author2):
    return Book.objects.filter(Q(author__name=author1) | Q(author__name=author2))


def get_books_excluding_author(author_name):
    return Book.objects.exclude(author__name=author_name)


def get_or_create_book(**kwargs):
    obj, created = Book.objects.get_or_create(**kwargs)
    return obj, created


def delete_book_by_id(book_id):
    deleted, _ = Book.objects.filter(id=book_id).delete()
    return deleted > 0


def soft_delete_book(book_id):
    updated = Book.objects.filter(id=book_id).update(is_deleted=True)
    return updated > 0


def get_author_book_count():
    return Book.objects.values("author__name").annotate(total=Count("id"))


# ------------------------------
# Collection Queries
# ------------------------------


def get_all_collections():
    return Collection.objects.prefetch_related("books").all()


def get_collection_by_name(name):
    return Collection.objects.prefetch_related("books").get(name=name)
