from django import forms
from .models import Book, Author, Publisher

class BookForm(forms.Form):
    name = forms.CharField( max_length=255, required=True)
    inventory = forms.IntegerField(min_value=0)
    price = forms.IntegerField()
    discount = forms. IntegerField(max_value=100, min_value=0)
    publisher = forms.ModelChoiceField(queryset=Publisher.objects.all())
    author = forms.ModelChoiceField(queryset=Author.objects.all())

