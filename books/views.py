from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Book, Author, Publisher
from .forms import BookForm
from django.forms.models import model_to_dict



def book_list(request):
    books = list(Book.objects.values())
    return JsonResponse({'books': books})

def author_list(request):
    authors = list(Author.objects.values())
    return JsonResponse({'authors': authors})

def publisher_list(request):
    publishers = list(Publisher.objects.values())
    return JsonResponse({'publishers': publishers})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/books/book-list/')
    else:
        form = BookForm()
    return render(request, 'books/book_create.html', {'form': form})


def get_book(request, id):
    try:
        book = Book.objects.get(id=id)
        book_dict = model_to_dict(book)
        return JsonResponse({'book': book_dict})
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book not found'}, status=404)

def home_page(request):
    return render(request, 'temp/index.html')