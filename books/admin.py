from django.contrib import admin
from .models import Book, Author, Publisher

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author', 'inventory', 'price', 'active']
    list_filter = ['active']

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'active']

admin.site.register(Publisher, PublisherAdmin)