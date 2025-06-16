from django.contrib import admin
from .models import Profile, Author, Publisher, Book, Collection

admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Collection)
