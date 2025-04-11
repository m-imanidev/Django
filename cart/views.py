from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from books.models import Book
from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    return render(request, "cart.html", {"cart": cart})


@csrf_exempt
def cart_add(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        quantity = int(request.POST.get("quantity", 1))

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return JsonResponse({"success": False, "message": "book was not found", "type": "danger"})

        cart = Cart(request)
        cart.add(book, quantity)

        return JsonResponse({"success": True, "message": "Book added to cart", "type": "success"})

    return JsonResponse({"success": False, "message": "Request is invalid", "type": "danger"})


def cart_remove(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return JsonResponse({"success": False, "message": "book was not found", "type": "danger"})

        cart = Cart(request)
        cart.remove(book)

        return JsonResponse({"success": True, "message": "Book removed from cart", "type": "success"})

    return JsonResponse({"success": False, "message": "Request is invalid", "type": "danger"})
