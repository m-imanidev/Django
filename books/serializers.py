from rest_framework import serializers

from .views import Book, Publisher, Author

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.ModelSerializer):
    publisher = serializers.PrimaryKeyRelatedField(queryset=Publisher.objects.all())
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())
    class Meta:
        model = Book
        fields = ['id', 'name', 'publisher', 'author', 'inventory', 'price', 'discount']
        extra_kwargs = {
            'author': {'required': True},
            'publisher': {'required': True}
        }