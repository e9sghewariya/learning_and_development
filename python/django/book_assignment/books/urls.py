from django.urls import path


from .views import (
    home,
    AuthorDetailView,
    AuthorListView,
    ProfileListView,
    ProfileDetailView,
    CollectionListView,
    CollectionDetailView,
    PublisherDetailView,
    PublisherListView,
    BookDetailView,
    BookListView,
)


app_name = "books"

urlpatterns = [
    path("", home, name="home"),
    path("profiles/", ProfileListView.as_view(), name="profile_list"),
    path("profiles/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("authors/", AuthorListView.as_view(), name="author_list"),
    path("authors/<int:pk>/", AuthorDetailView.as_view(), name="author_detail"),
    path("publishers/", PublisherListView.as_view(), name="publisher_list"),
    path(
        "publishers/<int:pk>/", PublisherDetailView.as_view(), name="publisher_detail"
    ),
    path("books/", BookListView.as_view(), name="book_list"),
    path("books/<int:pk>/", BookDetailView.as_view(), name="book_detail"),
    path("collections/", CollectionListView.as_view(), name="collection_list"),
    path(
        "collections/<int:pk>/",
        CollectionDetailView.as_view(),
        name="collection_detail",
    ),
]
