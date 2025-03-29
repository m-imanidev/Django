from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    BookListView, create_book , BookDetailView,
    profile_user, update_book, AuthorListView,
    create_author, AuthorDetailView, PublisherListView,
    PublisherDetailView, publisher_create
)

urlpatterns = [
    path('books/', BookListView.as_view()),
    path('books/create/', create_book),
    path('books/<int:pk>/', BookDetailView.as_view()),
    path('books/<int:pk>/update/', update_book),

    path('authors/', AuthorListView.as_view()),
    path('authors/<int:pk>/', AuthorDetailView.as_view()),
    path('authors/create/', create_author),

    path('publishers/', PublisherListView.as_view()),
    path('publishers/<int:pk>/', PublisherDetailView.as_view()),
    path('publishers/create/', publisher_create),

    path('token/', obtain_auth_token, name='api_token_auth'),
    path('profile/', profile_user),
]
