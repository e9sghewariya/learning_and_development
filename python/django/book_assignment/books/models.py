from datetime import date, timedelta
import random, uuid
from django.db import models
from django.utils.text import slugify
from django.db.models import Q, Count


# Profile Model


class Profile(models.Model):
    slug = models.SlugField(unique=True, max_length=100)
    username = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.username)
        super().save(*args, **kwargs)


class Author(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="author"
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def get_all_names(cls):
        return list(cls.objects.values_list("name", flat=True))

    @classmethod
    def get_all_names_and_profiles(cls):
        return list(
            cls.objects.select_related("profile").values(
                "name", "profile__phone", "profile__address"
            )
        )

    @classmethod
    def with_more_than_two_books(cls):
        return cls.objects.annotate(book_count=Count("books")).filter(book_count__gt=2)

    class Meta:
        verbose_name = "Author"


class Publisher(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    website = models.URLField()
    email = models.EmailField()
    address = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Publisher"
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_publisher_name")
        ]


class Book(models.Model):
    GENRE_CHOICES = [
        ("horror", "Horror"),
        ("self_help", "Self Help"),
        ("adventure", "Adventure"),
        ("others", "Others"),
    ]

    slug = models.SlugField(max_length=100, unique=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    title = models.CharField(max_length=200)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name="books"
    )
    date_of_pub = models.DateField()
    is_deleted = models.BooleanField(default=False)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES, default="others")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.author.name}")
        super().save(*args, **kwargs)

    @classmethod
    def by_author_name_starting_with_a(cls):
        return cls.objects.filter(author__name__istartswith="a")

    @classmethod
    def by_author_name(cls, name):
        return cls.objects.filter(author__name=name)

    @classmethod
    def by_author_and_publisher(cls, author_name, publisher_name):
        return cls.objects.filter(
            author__name=author_name, publisher__name=publisher_name
        )

    @classmethod
    def by_author_name_ending_with_a(cls):
        return cls.objects.filter(author__name__iendswith="a")

    @classmethod
    def by_publication_year(cls, year):
        return cls.objects.filter(date_of_pub__year=year)

    @classmethod
    def by_publisher_name(cls, name):
        return cls.objects.filter(publisher__name=name)

    @classmethod
    def get_or_create_book(cls, **kwargs):
        obj, created = cls.objects.get_or_create(**kwargs)
        return obj, created

    @classmethod
    def by_publisher_website(cls, website):
        return cls.objects.filter(publisher__website=website)

    @classmethod
    def author_book_count(cls):
        return cls.objects.values("author__name").annotate(total=Count("id"))

    @classmethod
    def by_publisher_names(cls, names):
        return cls.objects.filter(publisher__name__in=names)

    @classmethod
    def by_authors(cls, author1, author2):
        return cls.objects.filter(Q(author__name=author1) | Q(author__name=author2))

    @classmethod
    def excluding_author(cls, author):
        return cls.objects.exclude(author__name=author)

    @classmethod
    def delete_book(cls, book_id):
        deleted, _ = cls.objects.filter(id=book_id).delete()
        return deleted > 0

    @classmethod
    def soft_delete_book(cls, book_id):
        updated = cls.objects.filter(id=book_id).update(is_deleted=True)
        return updated > 0

    class Meta:
        verbose_name = "Book"
        ordering = ["date_of_pub"]
        constraints = [
            models.UniqueConstraint(
                fields=["author", "title", "date_of_pub"],
                name="unique_author_title_date",
            )
        ]


# --------------------
# Collection Model
# --------------------
class Collection(models.Model):
    slug = models.SlugField(max_length=100, unique=True, blank=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    books = models.ManyToManyField(Book, related_name="collections")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Book_Collection"
        db_table = "book_collection"


# --------------------
# Data Generation
# --------------------
def bulk_insertion_of_data():
    N = 50000  # You can set to 50000 later
    print("Creating profiles...")
    profiles = [
        Profile(
            username=f"user{i}",
            email=f"user{i}_{uuid.uuid4().hex[:8]}@example.com",
            phone=f"+91-9990{i%10000:05}",
            address=f"Address {i}",
            slug=f"user{i}",
        )
        for i in range(N)
    ]
    Profile.objects.bulk_create(profiles, batch_size=1000)

    # Retrieve profiles with primary keys populated
    profiles = list(Profile.objects.all()[:N])

    print("Creating authors...")
    authors = [
        Author(
            name=f"Author {i}",
            slug=f"author-{i}",
            profile=profiles[i],
        )
        for i in range(N)
    ]
    Author.objects.bulk_create(authors, batch_size=1000)

    print("Creating publishers...")
    publishers = [
        Publisher(
            name=f"Publisher {i}",
            slug=f"publisher-{i}",
            website=f"https://publisher{i}.com",
            email=f"contact@publisher{i}.com",
            address=f"Publisher Address {i}",
        )
        for i in range(N)
    ]
    Publisher.objects.bulk_create(publishers, batch_size=1000)

    print("Creating books...")
    authors = list(Author.objects.all()[:N])
    publishers = list(Publisher.objects.all()[:N])
    books = [
        Book(
            title=f"Book Title {i}",
            slug=f"book-title-{i}",
            author=random.choice(authors),
            publisher=random.choice(publishers),
            date_of_pub=date.today() - timedelta(days=random.randint(0, 3650)),
            genre=random.choice([g[0] for g in Book.GENRE_CHOICES]),
        )
        for i in range(N)
    ]
    Book.objects.bulk_create(books, batch_size=1000)

    print("Creating collections...")
    collections = [
        Collection(name=f"Collection {i}", slug=f"collection-{i}") for i in range(N)
    ]
    Collection.objects.bulk_create(collections, batch_size=1000)

    print("Creating many-to-many links...")
    books = list(Book.objects.all()[:N])
    collections = list(Collection.objects.all()[:N])
    through_model = Collection.books.through
    m2m_links = []
    for collection in collections:
        sample_books = random.sample(books, 3)
        for book in sample_books:
            m2m_links.append(
                through_model(collection_id=collection.id, book_id=book.id)
            )

    through_model.objects.bulk_create(m2m_links, batch_size=1000)

    print("✅ Data insertion completed.")
