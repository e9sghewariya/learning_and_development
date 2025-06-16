from django.db import models

# Create your models here.

class Author(models.Model):
    """
    Model representing an author.
    """
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()

    def __str__(self):
        """
        String for representing the Author object.
        """
        return str(self.name)


class Book(models.Model):
    """
    Model representing a book.
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    published_year = models.IntegerField()

    def __str__(self):
        """
        String for representing the Book object.
        """
        return str(self.title)