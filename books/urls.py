# from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('book-list/', views.book_list),
    path('author-list/', views.author_list),
    path('publisher-list/', views.publisher_list),
    path('books/create/', views.book_create),
    path('books/<int:id>/', views.get_book),
    path('', views.home_page, name='home'),
]